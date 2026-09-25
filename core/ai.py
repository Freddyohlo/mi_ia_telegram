from groq import Groq
from config import GROQ_API_KEY, MODEL

if not GROQ_API_KEY:
    raise RuntimeError(
        "Falta GROQ_API_KEY. Configúrala en el archivo .env "
        "(puedes copiar .env.example como plantilla)."
    )

cliente = Groq(api_key=GROQ_API_KEY)


def responder(prompt=None, mensajes=None):

    if mensajes is None:
        mensajes = [
            {
                "role": "user",
                "content": prompt
            }
        ]

    respuesta = cliente.chat.completions.create(
        model=MODEL,
        messages=mensajes
    )

    return respuesta.choices[0].message.content


def decidir_herramienta(pregunta):

    prompt = f"""
Eres el planificador de un agente de IA.

Debes responder SOLO una palabra.

Las opciones son:

INTERNET
CHAT

Utiliza INTERNET únicamente si necesitas información reciente o información que probablemente no conozcas.

Ejemplos

¿Qué es Python?
CHAT

¿Qué es OpenAI?
CHAT

¿Cuánto vale el dólar hoy?
INTERNET

Noticias de Tesla
INTERNET

Pregunta:

{pregunta}
"""

    return responder(prompt=prompt).strip().upper()