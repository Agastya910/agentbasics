import requests

from config import MODEL, OLLAMA_API_KEY, OLLAMA_URL


def chat(messages, tools):
    resp = requests.post(OLLAMA_URL, headers={"Authorization": f"Bearer {OLLAMA_API_KEY}"}, json={
        "model": MODEL,
        "messages": messages,
        "tools": tools,
        "stream": False,
    })
    resp.raise_for_status()
    return resp.json()["message"]