def necesita_internet(pregunta):

    palabras = [
        "hoy",
        "actual",
        "actualidad",
        "última",
        "último",
        "buscar",
        "internet",
        "precio",
        "noticia",
        "clima",
        "cotización",
        "dólar"
    ]

    pregunta = pregunta.lower()

    return any(p in pregunta for p in palabras)