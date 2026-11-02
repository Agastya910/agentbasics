from agent.loop import run
from agent.prompt import SYSTEM

messages = [{"role": "system", "content": SYSTEM}]
while (user := input("\nyou: ").strip()) not in ("q", "quit"):
    messages.append({"role": "user", "content": user})
    print("\nagent:", run(messages))