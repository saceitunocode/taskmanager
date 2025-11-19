from task_manager import TaskManager
from ai_service import create_simple_task

def print_menu():
    print("\n¡Bienvenido al gestor de tareas inteligente!\n")
    print("Comandos disponibles:")
    print("add <description> --- Añadir una nueva tarea")
    print("addia <description> - Añadir una nueva tarea utilizando la IA")
    print("list ---------------- Mostrar todas las tareas")
    print("complete <id> ------- Marcar una tarea como completada")
    print("delete <id> --------- Eliminar una tarea")
    print("exit ---------------- Salir de la aplicación\n")

def main():

    task_manager = TaskManager()

    while True:
        print_menu()

        choice = input("Introduce un comando: ").strip().split(' ', 1)

        match choice[0]:
            case "add":
                if len(choice) < 2:
                    print("\nError: Se requiere una descripción para la tarea")
                else:
                    task_manager.add_task(choice[1])

            case "addia":
                if len(choice) < 2:
                    print("\nError: Se requiere una descripción para la tarea")
                else:
                    subtasks = create_simple_task(choice[1])
                    if subtasks and not subtasks[0].startswith("Error"):
                        print("\nSubtareas generadas por IA:")
                        for subtask in subtasks:
                            task_manager.add_task(subtask)
                    else:
                        print(f"\n{subtasks[0]}")
                        break

            case "list":
                task_manager.list_task()

            case "complete":
                if len(choice) < 2 or not choice[1].isdigit():
                    print("\nError: Se requiere un ID de tarea válido")
                else:
                    task_manager.complete_task(int(choice[1]))

            case "delete":
                if len(choice) < 2 or not choice[1].isdigit():
                    print("\nError: Se requiere un ID de tarea válido")
                else:
                    task_manager.delete_task(int(choice[1]))

            case "exit":
                print("\nSaliendo de la aplicación. ¡Hasta luego!")
                break

            case _:
                print("\nError: Comando desconocido")

if __name__ == "__main__":
    main()