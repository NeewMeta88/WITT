# 🌙 WITT — Stateless LangGraph Chatbot

This is a minimal project using **LangGraph** to implement a **stateless chatbot**. The bot uses a single tool `get_current_time()` when asked for the current time and responds to all other inputs using an LLM. It supports both OpenAI and **local models via Ollama**.

---

## 🚧 What it does

- Stateless LangGraph flow — no memory or database.
- One tool:
  ```python
  def get_current_time() -> dict:
      """Return the current UTC time in ISO-8601 format.
      Example → {"utc": "2025‑05‑21T06:42:00Z"}"""
  ```
- Two nodes:
  - `time_node` — called if user asks about time.
  - `llm_node` — replies to all other messages.
- Compatible with **OpenAI** and **Ollama** (local LLM).

---

## 🛠 How to Run

```bash
git clone https://github.com/NeewMeta88/WITT
cd witt

python -m venv .venv
source .venv/bin/activate     # or .venv\Scripts\activate on Windows

pip install -r requirements.txt
langgraph dev
```

> This starts a local dev server with the graph in memory.

---

## ☁️ Using OpenAI

1. **Create your own OpenAI API key:**

   - Visit [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
   - Sign in or create an account
   - Click **“Create new secret key”**
   - Copy and save the key somewhere safe

2. **Update the existing `.env` file in the project root directory:**

   Replace the placeholder with your actual API key:

   ```env
   OPENAI_API_KEY=sk-...your_actual_key_here...


---

## ✅ Spec Compliance

- ✅ Stateless LangGraph chat flow
- ✅ Uses exactly one tool (`get_current_time`)
- ✅ No memory or database
- ✅ Works with `langgraph dev`
- ✅ Minimal repo: one `.py` file, `requirements.txt`, and `README.md`

---

## 🧪 Example

**Input:**
```
What time is it?
```

**Output:**
```json
{"utc": "2025-05-29T15:04:00Z"}
```

Any other input is processed normally by the LLM.
