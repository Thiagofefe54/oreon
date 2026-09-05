"""
Cliente da Groq API para o OREON.
Usa o histórico do memory_manager como contexto e salva a resposta gerada.
"""

import os
from dotenv import load_dotenv
from groq import AsyncGroq

from memory.memory_manager import memory_manager

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "openai/gpt-oss-120b"

client = AsyncGroq(api_key=GROQ_API_KEY)


async def ask_groq(user_message: str) -> str:
    # Salva a mensagem do usuário na memória antes de montar o contexto
    memory_manager.add_message("user", user_message)

    history = memory_manager.get_history()

    response = await client.chat.completions.create(
        model=MODEL_NAME,
        messages=history,
    )

    reply_text = response.choices[0].message.content

    memory_manager.add_message("assistant", reply_text)

    return reply_text
