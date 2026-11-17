import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"
LEGACY_ENV_FILE = PROJECT_ROOT / "AI_Chatbot" / "venv" / ".env"
ACTIVE_ENV_FILE = (
    ENV_FILE
    if ENV_FILE.is_file() or not LEGACY_ENV_FILE.is_file()
    else LEGACY_ENV_FILE
)
load_dotenv(dotenv_path=ACTIVE_ENV_FILE)


def get_api_key() -> str | None:
    api_key = os.getenv("COHERE_API_KEY", "").strip()
    return api_key or None
