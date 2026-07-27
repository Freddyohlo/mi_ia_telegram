import os
from threading import Thread

from flask import Flask
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

from agente import responder_agente

from memoria.memoria import guardar
from memoria.memoria import leer


# ----------------------------
# Servidor Flask para Render
# ----------------------------

web = Flask(__name__)


@web.route("/")
def home():
    return "Bot de Telegram funcionando correctamente."


def iniciar_web():
    puerto = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=puerto)


# ----------------------------
# Telegram
# ----------------------------

TOKEN = "8768492730:AAFvUzDkPI7rNVCCle1Pssfo1JdNkNpweDw"


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    pregunta = update.message.text

    # Leemos la memoria del usuario
    memoria = leer(chat_id)

    print("MEMORIA:", memoria)

    # Guardado de prueba
    if pregunta.lower().startswith("me llamo "):

        nombre = pregunta[9:].strip()

        guardar(chat_id, "nombre", nombre)

        print("Nombre guardado:", nombre)

    try:

        respuesta = responder_agente(chat_id, pregunta)

    except Exception as e:

        print(f"Error: {e}")

        respuesta = "Ocurrió un problema procesando tu consulta."

    await update.message.reply_text(respuesta)


def iniciar_bot():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            responder
        )
    )

    print("🤖 Bot iniciado...")

    app.run_polling()


if __name__ == "__main__":

    Thread(target=iniciar_web).start()

    iniciar_bot()















