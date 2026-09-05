"""
Gerenciador de memória do OREON.
Persiste o histórico de mensagens em um arquivo JSON local (memory.json).
get_history() sempre retorna o System Prompt + as últimas 20 mensagens (janela deslizante).
"""

import json
import os
from pathlib import Path

MEMORY_FILE = Path(__file__).resolve().parent / "memory.json"
HISTORY_WINDOW = 20

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "Você é OREON, um assistente de desktop de alta performance criado pelo "
        "engenheiro Thiago Feijó da Silva. Você não é o ChatGPT nem a OpenAI. "
        "Seja direto, maduro, sem excesso de emojis e foque em eficiência."
    ),
}


class MemoryManager:
    def __init__(self, memory_file: Path = MEMORY_FILE):
        self.memory_file = memory_file
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def add_message(self, role: str, content: str):
        history = self._read_raw()
        history.append({"role": role, "content": content})
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

    def _read_raw(self) -> list:
        try:
            with open(self.memory_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def get_history(self) -> list:
        """Retorna o System Prompt + as últimas HISTORY_WINDOW mensagens."""
        raw = self._read_raw()
        window = raw[-HISTORY_WINDOW:] if len(raw) > HISTORY_WINDOW else raw
        return [SYSTEM_PROMPT, *window]

    def clear_history(self):
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump([], f)


memory_manager = MemoryManager()