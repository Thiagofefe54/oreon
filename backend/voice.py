import edge_tts
import asyncio
import tempfile
import os
from playsound import playsound
import speech_recognition as sr

async def _gerar_audio(texto: str, arquivo: str):
    communicate = edge_tts.Communicate(texto, voice="pt-BR-AntonioNeural")
    await communicate.save(arquivo)

def falar(texto: str):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        arquivo = f.name
    asyncio.run(_gerar_audio(texto, arquivo))
    playsound(arquivo)
    os.remove(arquivo)

def ouvir() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Ouvindo...")
        audio = r.listen(source, timeout=5)
    try:
        texto = r.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""