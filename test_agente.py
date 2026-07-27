from agente import responder_agente

while True:

    pregunta = input("\nTú: ")

    if pregunta.lower() == "salir":
        break

    respuesta = responder_agente(pregunta)

    print("\nAgente:\n")

    print(respuesta)