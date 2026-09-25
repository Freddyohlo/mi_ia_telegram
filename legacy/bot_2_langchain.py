# ==============================================================================
# LEGACY / NO USAR EN PRODUCCIÓN
# ==============================================================================
# Primera versión experimental del bot, construida con `pyTelegramBotAPI`
# (telebot) y LangChain. Fue reemplazada por la versión modular actual
# (`bot.py` + `agente.py` + `core/` + `tools/`).
#
# Se conserva solo como referencia histórica. Sus dependencias
# (`telebot`, `langchain`, `langchain_community`, `langchain_groq`)
# NO están en `requirements.txt`.
# ==============================================================================

import os
from threading import Thread

import telebot
from flask import Flask
from langchain.agents import AgentType, initialize_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq

from config import GROQ_API_KEY, TELEGRAM_TOKEN

app = Flask('')


@app.route('/')
def home():
    return "Bot activo"


Thread(
    target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080))),
    daemon=True,
).start()


bot = telebot.TeleBot(TELEGRAM_TOKEN)
llm = ChatGroq(api_key=GROQ_API_KEY, model_name="llama-3.1-8b-instant")
search_tool = DuckDuckGoSearchRun()

agent = initialize_agent(
    [search_tool],
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        respuesta = agent.run(message.text)
        bot.reply_to(message, respuesta)
    except Exception as e:
        bot.reply_to(message, "Error al procesar: " + str(e))


bot.infinity_polling()
