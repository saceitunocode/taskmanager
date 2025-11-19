import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_task(description):
    if not client.api_key:
        return ["Error: API key de OpenAI no está configurada"]
    
    try:
        prompt = f"""Desglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.

        Tarea: {description}

        Respuesta en formato de lista:
        - <subtarea 1>
        - <subtarea 2>
        - <subtarea 3>
        - etc.

        Responde solo con la lista de subtareas, una por linea, empezando cada linea con un guion y un espacio.
        """

        params = {
            "model": "gpt-5.1",
            "messages": [
                {"role": "system", "content": "Eres un asistente experto en gestion de tareas que ayuda a desglosar tareas complejas en subtareas simples y accionables."},
                {"role": "user", "content": prompt}
            ],
            "max_completion_tokens":300,
            "verbosity":"medium",
            "reasoning_effort":"medium"
        }

        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("- "):
                subtask = line[2:].strip()
                if subtask:
                    subtasks.append(subtask)
        
        return subtasks if subtasks else ["Error: No se han generado subtareas válidas"]

    except Exception:
        return ["Error: No se ha podido realizar la conexion con el servicio de IA"]