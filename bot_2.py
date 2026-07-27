import os
import telebot
from threading import Thread
from flask import Flask
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from config import TELEGRAM_TOKEN, GROQ_API_KEY

# 1. Configuración básica
app = Flask('')
@app.route('/')
def home():
    return "Bot activo"

Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080))), daemon=True).start()


bot = telebot.TeleBot(TELEGRAM_TOKEN)
llm = ChatGroq(api_key=GROQ_API_KEY, model_name="llama-3.1-8b-instant")
search_tool = DuckDuckGoSearchRun()

# ESTA ES LA CLAVE: Usamos la función clásica que es compatible con casi todo
agent = initialize_agent(
    [search_tool], 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Usamos .run(), que es el método universal en versiones estables
        respuesta = agent.run(message.text)
        bot.reply_to(message, respuesta)
    except Exception as e:
        bot.reply_to(message, "Error al procesar: " + str(e))

bot.infinity_polling()










