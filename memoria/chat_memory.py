HISTORIAL = {}

LIMITE = 12


def obtener_historial(chat_id):

    chat_id = str(chat_id)

    if chat_id not in HISTORIAL:

        HISTORIAL[chat_id] = [
            {
                "role": "system",
                "content": "Eres un asistente útil y preciso."
            }
        ]

    return HISTORIAL[chat_id]


def agregar_usuario(chat_id, mensaje):

    historial = obtener_historial(chat_id)

    historial.append(
        {
            "role": "user",
            "content": mensaje
        }
    )

    if len(historial) > LIMITE:

        HISTORIAL[str(chat_id)] = [
            historial[0]
        ] + historial[-(LIMITE-1):]


def agregar_asistente(chat_id, mensaje):

    historial = obtener_historial(chat_id)

    historial.append(
        {
            "role": "assistant",
            "content": mensaje
        }
    )









