from agente import responder_agente

# Chat de prueba por consola. Se usa un chat_id fijo para simular un usuario.
CHAT_ID_PRUEBA = "consola"

while True:

    pregunta = input("\nTú: ")

    if pregunta.lower() == "salir":
        break

    respuesta = responder_agente(CHAT_ID_PRUEBA, pregunta)

    print("\nAgente:\n")

    print(respuesta)