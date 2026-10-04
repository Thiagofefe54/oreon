"""
OREON Backend - Ponto de entrada da API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from core.groq_client import ask_groq

app = FastAPI(title="OREON Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    text: str


@app.get("/")
async def root():
    return {"status": "ok", "service": "oreon-backend"}


@app.post("/chat/text")
async def chat_text(request: ChatRequest):
    reply = await ask_groq(request.text)
    return {"reply": reply}


@app.post("/chat/voice")
async def chat_voice():
    # TODO: integrar Whisper (STT) + Groq
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
