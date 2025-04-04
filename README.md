# AI-Code-Generator
# 💻 AI Code Generator

Turn natural language into real code in seconds.  
Describe what you want, and this smart assistant will generate clean, working code using **CodeGemma** running locally via **Ollama**.

---
## 💡 Features

✅ **Natural Language to Code**  
Type something like `"Create a Python script to rename all files in a folder"` — and get the code.

✅ **Runs Locally via Ollama**  
No cloud, no API key required. Powered by [Ollama](https://ollama.com) + CodeGemma.

✅ **Modern UI with Streamlit**  
Fast, responsive, and accessible from your browser.

✅ **Multi-purpose Code Generation**  
From Python automation to web snippets, CLI tools to scraping scripts.

✅ **Offline & Private**  
No data leaves your machine. Perfect for secure or air-gapped environments.

---

## 🖥️ Built With

- [🧠 Ollama](https://ollama.com/) – Local LLM orchestration
- [🦙 CodeGemma](https://ai.google.dev/gemma) – Code generation model by Google
- [📊 Streamlit](https://streamlit.io/) – UI framework for interactive apps
- `subprocess`, `os` – For secure shell command execution

---

## 🛠️ Installation

### 1. Install [Ollama](https://ollama.com)  
Follow setup instructions for your OS.

### 2. Pull the CodeGemma model
```bash
ollama pull codegemma