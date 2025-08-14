# AIAgent

**A simple AI agent that automatically locates and patches code bugs using Google Gemini 2.0 Flash.** Built as part of a Boot.dev project.

---

##  Description

Why did I build this? Because Boot.dev told me to—and because machine sloths like me just can’t resist having AI do the debugging while I sip my coffee.
This project scans your code, spots bugs, and attempts fixes using the Gemini 2.0 Flash model. That’s it. No magic, just AI (and some caffeine).

The `calculator/` directory is just a toy project used for testing the AI — you can replace it with whatever code you actually want to debug.

---

##  Getting Started

Just clone it, install dependencies, and run it. No hand‑holding.

### Prerequisites

- Python 3.x
- Access to Google Gemini 2.0 Flash (API keys or credentials).
- [uv](https://github.com/astral-sh/uv) installed.

### Installation

```bash
git clone https://github.com/Batyr-R/AIAgent.git
cd AIAgent
uv sync
```

---

##  Usage

Before running, **edit** `config.py` and set `working_directory` to the folder containing the code you want scanned and fixed.

Run the AI agent:

```bash
uv run main.py
```

It’ll scan the target code, sniff out bugs, and attempt fixes. `prompts.py` contains the AI’s behavior instructions.

---

##  Project Structure

```
AIAgent/
├── calculator/          # just for test runs — not required for your usage
├── call_function.py     # bridge between your code and Gemini
├── config.py            # configure API keys, working directory, and behavior
├── main.py              # entry point — kick off the bug hunt
├── prompts.py           # definitions of behavior instructions
├── pyproject.toml       # project metadata & dependencies
├── README.md            # duh, you’re reading it
└── uv.lock              # lockfile for dependencies
```

---
