# AIAgent

**A simple AI agent that automatically locates and patches code bugs using Google Gemini 2.0 Flash.** Built as part of a Boot.dev project.

---

##  Description

Why did I build this? Because Boot.dev told me to—and because machine sloths like me just can’t resist having AI do the debugging while I sip my coffee.  
This project scans your code, spots bugs, and attempts fixes using the Gemini 2.0 Flash model. That’s it. No magic, just AI (and some caffeine).

---

##  Getting Started

Just clone it, install dependencies, and run it. No hand‑holding.

### Prerequisites

- Python 3.x  
- Access to Google Gemini 2.0 Flash (API keys or credentials).

### Installation

```bash
git clone https://github.com/Batyr-R/AIAgent.git
cd AIAgent
pip install -r requirements.txt
```

---

##  Usage

Run this gem and watch the AI do its thing:

```bash
python main.py
```

It’ll scan dangerous code, sniff out bugs, and attempt fixes. Check `config.py` to tweak behavior. `prompts.py` has fun instructions for Gemini.

---

##  Project Structure

```
AIAgent/
├── call_function.py     # bridge between your code and Gemini
├── config.py            # configure API keys & behavior
├── main.py              # entry point — kick off the bug hunt
├── prompts.py           # definitions of behavior instructions
├── pyproject.toml       # project metadata & dependencies
├── README.md            # duh, you’re reading it
└── uv.lock              # lockfile for dependencies
```

---

##  Contribute

Want to help? Code is open—just open a PR or issue. Make it smarter. Make it faster. Make it not embarrass you in a job interview.

---

##  License

Put your preferred license here. MIT, GPL, or whatever — just pick something and move on.
