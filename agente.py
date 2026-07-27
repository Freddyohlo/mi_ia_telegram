from core.ai import responder
from core.ai import decidir_herramienta
from tools.internet import buscar_web

from memoria.chat_memory import (
    obtener_historial,
    agregar_usuario,
    agregar_asistente
)
from memoria.memoria import leer


def responder_agente(chat_id, pregunta):

    decision = decidir_herramienta(pregunta)

    print(f"Herramienta elegida -> {decision}")

    agregar_usuario(chat_id, pregunta)

    historial = obtener_historial(chat_id)

    # Cargamos la memoria persistente
    memoria = leer(chat_id)

    if memoria:

        texto_memoria = "Información conocida del usuario:\n\n"

        for clave, valor in memoria.items():
            texto_memoria += f"{clave}: {valor}\n"

        historial.insert(
            1,
            {
                "role": "system",
                "content": texto_memoria
            }
        )

    if decision == "INTERNET":

        resultados = buscar_web(pregunta)

        contexto = ""

        for r in resultados:

            contexto += f"""
Título:
{r['titulo']}

Descripción:
{r['descripcion']}

URL:
{r['url']}

"""

        historial.append(
            {
                "role": "system",
                "content": f"""
Utiliza esta información de Internet para responder.

{contexto}

Reglas:

- Usa la información cuando sea relevante.
- Si hay varias fuentes, puedes resumirlas.
- Menciona la fuente cuando corresponda.
- No inventes información.
"""
            }
        )

    respuesta = responder(mensajes=historial)

    agregar_asistente(chat_id, respuesta)

    return respuesta