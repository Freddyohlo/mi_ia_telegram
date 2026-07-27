from ddgs import DDGS


def buscar_web(consulta, max_resultados=5):

    if "dólar" in consulta.lower() or "dolar" in consulta.lower():
        consulta += " Chile peso chileno CLP"

    resultados = []

    with DDGS() as buscador:

        for r in buscador.text(
            consulta,
            max_results=max_resultados
        ):

            resultados.append({
                "titulo": r.get("title"),
                "url": r.get("href"),
                "descripcion": r.get("body")
            })

    return resultados



