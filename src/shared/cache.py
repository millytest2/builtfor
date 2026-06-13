"""File-based response cache. Avoids re-paying for / re-pulling the same API
results — keeps live runs cheap and re-runnable."""
import hashlib
import json
import time
from pathlib import Path
from typing import Optional


class HttpCache:
    def __init__(self, directory: str = "data/cache", ttl_hours: float = 168):
        self.dir = Path(directory)
        self.dir.mkdir(parents=True, exist_ok=True)
        self.ttl = ttl_hours * 3600

    def _path(self, key: str) -> Path:
        digest = hashlib.sha256(key.encode()).hexdigest()[:24]
        return self.dir / f"{digest}.json"

    def get(self, key: str) -> Optional[dict]:
        p = self._path(key)
        if p.exists():
            try:
                data = json.loads(p.read_text())
            except json.JSONDecodeError:
                return None
            if time.time() - data["ts"] < self.ttl:
                return data["value"]
        return None

    def set(self, key: str, value: dict) -> None:
        self._path(key).write_text(json.dumps({"ts": time.time(), "value": value}))
