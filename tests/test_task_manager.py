import json
from pathlib import Path

import pytest

from task_manager import TaskManager


def test_add_task_creates_task_and_saves_file(tmp_path, capsys):
    # Arrange
    TaskManager.FILENAME = str(tmp_path / "tasks.json")
    manager = TaskManager()

    # Act
    manager.add_task("Write tests")
    captured = capsys.readouterr()

    # Assert: stdout contains confirmation and description
    assert "Tarea añadida" in captured.out
    assert "Write tests" in captured.out

    # Assert: file was created and contains the correct data
    data = json.loads(Path(TaskManager.FILENAME).read_text())
    assert isinstance(data, list)
    assert len(data) == 1
    item = data[0]
    assert item["id"] == 1
    assert item["description"] == "Write tests"
    assert item["complete"] is False


def test_complete_task_marks_and_persists(tmp_path, capsys):
    # Arrange: prepopulate tasks.json with a task id 1
    file_path = tmp_path / "tasks.json"
    preexisting = [{"id": 1, "description": "tarea", "complete": False}]
    file_path.write_text(json.dumps(preexisting, indent=4))

    TaskManager.FILENAME = str(file_path)
    manager = TaskManager()

    # Act
    manager.complete_task(1)
    captured = capsys.readouterr()

    # Assert: stdout contains completion message
    assert "Tarea completada" in captured.out

    # Assert: in-memory state updated
    assert any(t.id == 1 and t.completed for t in manager._tasks)

    # Assert: file persisted the completed status
    data = json.loads(file_path.read_text())
    assert data[0]["complete"] is True


def test_delete_task_removes_and_persists(tmp_path, capsys):
    # Arrange: two tasks in file
    file_path = tmp_path / "tasks.json"
    preexisting = [
        {"id": 1, "description": "first", "complete": False},
        {"id": 2, "description": "second", "complete": False},
    ]
    file_path.write_text(json.dumps(preexisting, indent=4))

    TaskManager.FILENAME = str(file_path)
    manager = TaskManager()

    # Act
    manager.delete_task(1)
    captured = capsys.readouterr()

    # Assert: stdout mentions elimination
    assert "Tarea eliminada" in captured.out

    # Assert: in-memory no longer contains id 1
    assert all(t.id != 1 for t in manager._tasks)

    # Assert: file no longer contains id 1
    data = json.loads(file_path.read_text())
    ids = [item["id"] for item in data]
    assert 1 not in ids
    assert 2 in ids


def test_load_sets_next_id(tmp_path):
    # Arrange: prepopulate with a high id
    file_path = tmp_path / "tasks.json"
    preexisting = [{"id": 5, "description": "ex", "complete": False}]
    file_path.write_text(json.dumps(preexisting, indent=4))

    TaskManager.FILENAME = str(file_path)

    # Act
    manager = TaskManager()

    # Assert: next id should be max(id) + 1
    assert manager._next_id == 6


def test_list_task_outputs_tasks(tmp_path, capsys):
    # Arrange
    TaskManager.FILENAME = str(tmp_path / "tasks.json")
    manager = TaskManager()

    manager.add_task("Task A")
    manager.add_task("Task B")

    # Act
    manager.list_task()
    captured = capsys.readouterr()

    # Assert: both tasks printed
    assert "Task A" in captured.out
    assert "Task B" in captured.out
