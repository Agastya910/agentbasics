This is the project that creates the most basic ai agent in the world.

pure python

LLM - Ollama 


Phase 0
send request to the ollama llm -- get response -- execute a function call


Phase 1, 2 ... so on

Give it more capabilities (More function calls.)



This AI agent is like any other script in your codebase. It gets triggered after some events, does some actions. 
What makes it different, is that it utilizes the Natural Language Processing capabilities of a sophisticated program like an LLM. 



LLM -- summarization. 

meeting ai agent , summarization of what was done in a meeting, ping people about their tasks. 


Learning : summarization of text would require some kind of nLp therefore this would be an ai agent. 


llm/ 
 -- ollama client.py - handles http requests and responses to and from the llm / websocket with the llm , 
 -- llm streaming.py - sse response prossessing, 

tools/
    -- 









---

# Running this project

A small calendar assistant, written as a plain Python loop with no agent framework. You chat with it in the terminal. It can list your events, find free time, and add, move or delete events in `data/calendar.json`.

## The LLM: Gemma on Ollama's cloud

- **Model:** this project uses Gemma, Google's open model family, with the tag `gemma4:31b-cloud` (set in `config.py`).
- **Where it runs:** on Ollama's cloud at `https://ollama.com/api/chat`, **not on your machine**. You don't need a GPU or a local Ollama install, but you do need an Ollama account, an API key and an internet connection.
- **What leaves your machine:** your messages, the system prompt, and any calendar events the agent reads are sent to Ollama's cloud.
- **Availability and limits:** these depend on Ollama's cloud service and your account. If the model tag stops working, change `MODEL` in `config.py`.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (recommended), or pip
- An [Ollama](https://ollama.com) account

## Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/Agastya910/agentbasics.git
   cd agentbasics
   ```

2. Sign in at [ollama.com](https://ollama.com) and create an API key at [ollama.com/settings/keys](https://ollama.com/settings/keys).

3. Create your `.env` file from the example.

   macOS/Linux:

   ```bash
   cp .env.example .env
   ```

   Windows PowerShell:

   ```powershell
   Copy-Item .env.example .env
   ```

4. Open `.env` and put in your key:

   ```
   OLLAMA_API_KEY=your_ollama_api_key_here
   ```

   `.env` is listed in `.gitignore`. Never commit it.

## Run

With uv, which creates the environment and installs dependencies for you:

```bash
uv run main.py
```

Or with pip:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Run it from the project root, because the calendar path is relative. Type `q` or `quit` to exit.

## Try it

The sample calendar has events on `2026-11-02`, and several of them are badly arranged on purpose. Try:

```
you: What's on my calendar on 2026-11-02?
you: Optimize that day for me.
you: Find me a free 30 minutes that day.
```

Tool calls are printed as they happen, for example `-> list_events({'date': '2026-11-02'})`.

## How it works

```
main.py                   terminal chat loop
agent/loop.py             the agent loop: call the LLM, run tools, repeat (max 10 steps)
agent/prompt.py           system prompt
llm/ollama_client.py      HTTP request to Ollama
tools/calendar_tools.py   the calendar functions
tools/schemas.py          tool descriptions sent to the model
config.py                 model, URL and file paths; loads .env
data/calendar.json        the calendar
```

Each turn, the model either replies in plain text, which ends the loop, or asks for tool calls. Tools run locally, their results go back to the model, and the loop continues.

## Known limitations

- "Pure Python" means no agent framework; the project does use the `requests` library.
- Asking before changing events is an instruction in the system prompt, not something the code enforces. The model could change `data/calendar.json` without asking, so keep a copy if the data matters.
- Conversations are not saved between runs.
- There are no tests.
- `llm/streaming` from the notes above isn't built yet: responses are not streamed.

## Troubleshooting

| Error | Likely cause |
| --- | --- |
| `401 Unauthorized` | `OLLAMA_API_KEY` is missing or wrong in `.env` |
| `404 Not Found` | The model tag in `config.py` isn't available; pick a current one |
| `FileNotFoundError: data/calendar.json` | You're not running from the project root |
