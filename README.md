# TaskManager

Aplicación CLI en Python para gestionar tareas simples con persistencia en JSON.

## Descripción
TaskManager permite crear, listar, completar y eliminar tareas desde la terminal. Las tareas se guardan en un archivo `tasks.json` para mantener la persistencia entre sesiones.

## Estructura del proyecto
```
taskmanager/
├── main.py                # Interfaz CLI principal
├── task_manager.py        # Lógica de gestión de tareas
├── ai_service.py          # Servicio opcional para generación de subtareas con IA
├── requirements.txt       # Dependencias de ejecución
├── tasks.json             # Archivo de datos de tareas (generado automáticamente)
├── tests/
│   └── test_task_manager.py  # Pruebas unitarias con pytest
└── README.md              # Este archivo
```

## Características principales
- Añadir tareas con ID autoincremental.
- Listar todas las tareas.
- Marcar tareas como completadas.
- Eliminar tareas.
- Persistencia automática en `tasks.json`.
- Pruebas unitarias incluidas.
- Comando opcional para generación de subtareas con IA (`addia`).

## Requisitos
- Python 3.10 o superior.
- Dependencias de `requirements.txt`.
- Opcional: `pytest` para ejecutar tests.

## Instalación
Se recomienda usar un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install pytest  # Opcional, solo para desarrollo y testing
```

## Uso
Ejecuta la aplicación con:

```bash
python main.py
```

Comandos disponibles en el menú:
- `add <descripción>`: Añade una nueva tarea.
- `addia <descripción>`: (Opcional) Usa IA para generar subtareas.
- `list`: Muestra todas las tareas.
- `complete <id>`: Marca la tarea como completada.
- `delete <id>`: Elimina la tarea.
- `exit`: Salir de la aplicación.

## Formato de `tasks.json`
```json
[
  {
    "id": 1,
    "description": "Comprar leche",
    "complete": false
  }
]
```

## Pruebas
Para ejecutar los tests unitarios:

```bash
pytest -q
```

## Sugerencias de mejora
- Manejar errores de lectura/escritura en JSON.
- Validar el esquema de los datos.
- Añadir integración continua (CI) con GitHub Actions.
- Mejorar la interfaz y añadir más comandos.

## Licencia
MIT (puedes cambiarla según tu preferencia)

## Autor y contacto
Creador: saceitunocode  
Contacto: [saceituno92@gmail.com]
