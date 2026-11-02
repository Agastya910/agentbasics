import os
from pathlib import Path

env_file = Path(__file__).parent / ".env"
if env_file.exists():
    for line in env_file.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))

MODEL = "gemma4:31b-cloud"
OLLAMA_URL = "https://ollama.com/api/chat"
OLLAMA_API_KEY = os.environ.get("OLLAMA_API_KEY", "")
CAL_FILE = "data/calendar.json"
FMT = "%Y-%m-%dT%H:%M"
