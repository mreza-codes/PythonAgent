import json
import os

class MemoryStore:
    def __init__(self, path="memory/memory.json"):
        self.path = path
        if not os.path.exists(path):
            self._init_memory()

    def _init_memory(self):
        data = {
            "history": [],
            "thoughts": [],
            "actions": [],
            "retrievals": [],
            "states": [],
            "observations": []   # important!
        }
        self._save(data)

    def _load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def add(self, key, value):
        data = self._load()

        # Auto-create missing keys
        if key not in data:
            data[key] = []

        data[key].append(value)
        self._save(data)

    def get(self, key):
        return self._load().get(key, [])
