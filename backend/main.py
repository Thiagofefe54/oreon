from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
import asyncio
import os
from voice import falar

load_dotenv()

app = FastAPI()
executor = ThreadPoolExecutor()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

historico = [
    {
        "role": "system",
        "content": (
            "Você é OREON, um assistente pessoal inteligente do Thiago. "
            "Seja direto, eficiente e com personalidade. "
            "Responda sempre em português brasileiro."
        )
    }
]

class Mensagem(BaseModel):
    texto: str

@app.post("/chat")
async def chat(msg: Mensagem):
    historico.append({"role": "user", "content": msg.texto})
    
    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=historico,
        max_tokens=1024,
    )
    
    texto_resposta = resposta.choices[0].message.content
    historico.append({"role": "assistant", "content": texto_resposta})
    
    loop = asyncio.get_event_loop()
    loop.run_in_executor(executor, falar, texto_resposta)
    
    return {"resposta": texto_resposta}

@app.get("/status")
async def status():
    return {"status": "online"}

@app.post("/falar")
async def falar_rota(msg: Mensagem):
    loop = asyncio.get_event_loop()
    loop.run_in_executor(executor, falar, msg.texto)
    return {"status": "ok"}