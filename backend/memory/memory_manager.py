"""
Gerenciador de memória do OREON.
Persiste o histórico de mensagens em um arquivo JSON local (memory.json).
"""

import json
import os
from pathlib import Path

MEMORY_FILE = Path(__file__).resolve().parent / "memory.json"


class MemoryManager:
    def __init__(self, memory_file: Path = MEMORY_FILE):
        self.memory_file = memory_file
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def add_message(self, role: str, content: str):
        history = self.get_history()
        history.append({"role": role, "content": content})
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

    def get_history(self) -> list:
        try:
            with open(self.memory_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def clear_history(self):
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump([], f)


memory_manager = MemoryManager()
