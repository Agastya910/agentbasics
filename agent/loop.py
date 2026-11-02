import json

from llm.ollama_client import chat
from tools.schemas import TOOLS, SCHEMAS


def run(messages, max_steps=10):
    for _ in range(max_steps):
        msg = chat(messages, SCHEMAS)
        messages.append(msg)
        if not msg.get("tool_calls"):            # no tool call means the model is done
            return msg["content"]
        for call in msg["tool_calls"]:           # act, then show the model what happened
            name, args = call["function"]["name"], call["function"]["arguments"]
            print(f"  -> {name}({args})")
            try:
                result = TOOLS[name](**args)
            except Exception as e:
                result = {"error": str(e)}       # errors go back to the model, it can retry
            messages.append({"role": "tool", "content": json.dumps(result), "tool_name": name})
    return "(stopped: too many steps)"