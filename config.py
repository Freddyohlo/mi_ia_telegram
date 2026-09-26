# ==============================
# CONFIGURACIÓN DEL PROYECTO
# ==============================

import os

from dotenv import load_dotenv

load_dotenv()

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Modelo de IA
MODEL = os.getenv("MODEL", "llama-3.1-8b-instant")

# Memoria
MEMORY_LIMIT = int(os.getenv("MEMORY_LIMIT", "10"))