import json
import os

ARCHIVO_MEMORIA = os.path.join(
    os.path.dirname(__file__),
    "memoria.json"
)


def cargar_memoria():

    if not os.path.exists(ARCHIVO_MEMORIA):
        return {}

    with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_memoria(datos):

    with open(ARCHIVO_MEMORIA, "w", encoding="utf-8") as archivo:
        json.dump(
            datos,
            archivo,
            ensure_ascii=False,
            indent=4
        )


def guardar(chat_id, clave, valor):

    datos = cargar_memoria()

    chat_id = str(chat_id)

    if chat_id not in datos:
        datos[chat_id] = {}

    datos[chat_id][clave] = valor

    guardar_memoria(datos)


def recordar(chat_id, clave):

    datos = cargar_memoria()

    chat_id = str(chat_id)

    if chat_id in datos:
        return datos[chat_id].get(clave)

    return None


def leer(chat_id):

    datos = cargar_memoria()

    chat_id = str(chat_id)

    return datos.get(chat_id, {})


def olvidar(chat_id, clave):

    datos = cargar_memoria()

    chat_id = str(chat_id)

    if chat_id in datos:

        if clave in datos[chat_id]:

            del datos[chat_id][clave]

            guardar_memoria(datos)









