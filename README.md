# 🤖 Agente IA para Telegram

Bot de Telegram con inteligencia artificial que conversa con el usuario, recuerda
datos de cada persona y decide por sí solo cuándo buscar en Internet para
responder con información actualizada.

## ✨ Qué hace

- **Conversación con IA** — responde usando Groq (`llama-3.1-8b-instant`).
- **Búsqueda en Internet** — cuando la pregunta necesita información reciente
  (precios, noticias, clima), consulta DuckDuckGo y cita las fuentes.
- **Memoria por usuario** — guarda datos como el nombre y los reutiliza en
  conversaciones futuras.
- **Historial acotado** — mantiene el contexto reciente sin crecer sin límite.

## 🧠 Arquitectura

```
bot.py                    Punto de entrada: servidor Flask + polling de Telegram
agente.py                 Orquesta el flujo: memoria -> decisión -> respuesta
config.py                 Configuración y lectura de variables de entorno
core/
  ai.py                   Cliente de Groq y planificador (INTERNET / CHAT)
  router.py               Reglas por palabras clave (auxiliar)
tools/
  internet.py             Búsqueda web vía DuckDuckGo
memoria/
  chat_memory.py          Historial de conversación en memoria
  memoria.py              Memoria persistente por chat (JSON)
legacy/
  bot_2_langchain.py      Versión antigua (no usar, solo referencia)
```

## 🚀 Puesta en marcha

### 1. Requisitos

- Python 3.10 o superior
- Un token de bot de Telegram ([@BotFather](https://t.me/BotFather))
- Una API key de [Groq](https://console.groq.com/keys)

### 2. Instalación

```bash
git clone https://github.com/Freddyohlo/mi_ia_telegram.git
cd mi_ia_telegram
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configuración

Copia la plantilla y completa tus credenciales:

```bash
cp .env.example .env
```

```env
TELEGRAM_TOKEN=tu_token_de_botfather
GROQ_API_KEY=tu_api_key_de_groq
```

> ⚠️ El archivo `.env` **nunca** se sube al repositorio (ya está en `.gitignore`).

### 4. Ejecución

```bash
python bot.py
```

El bot levanta un pequeño servidor web (para plataformas como Render) y comienza
a escuchar mensajes de Telegram.

## 🧪 Pruebas manuales

```bash
python test_internet.py     # Verifica la búsqueda web
python probar_internet.py   # Consulta de ejemplo (valor del dólar)
python test_agente.py       # Chat por consola con el agente
```

## 🔐 Seguridad

- Las credenciales se leen desde variables de entorno, nunca desde el código.
- Si un token estuvo expuesto alguna vez, **revócalo en @BotFather** y genera uno nuevo.

## 📄 Licencia

Uso personal. Todos los derechos reservados.
