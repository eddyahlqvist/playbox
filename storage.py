# storage.py

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

def data_dir() -> Path:
    # playbox/ -> data/
    return Path(__file__).resolve().parent / "data"

def load_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default
    except json.JSONDecodeError as exc:
        raise ValueError("Corrupted JSON file") from exc

def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
