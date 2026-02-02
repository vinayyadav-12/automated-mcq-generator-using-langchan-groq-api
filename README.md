# MCQs Creator Application with LangChain 🧠🤖

A **production-ready LLM-powered application** that automatically generates **high-quality Multiple Choice Questions (MCQs)** from input text, PDFs, or notes, with **difficulty control, correct answers, and explanations**.

This project is ideal for **EdTech platforms, teachers, exam preparation tools, and AI portfolios**, showcasing prompt engineering, structured outputs, and robust JSON handling.

---

## 🚀 Features

* 📄 Input from text or PDF
* 🧠 AI-generated MCQs
* 🎯 Difficulty levels: Easy / Medium / Hard
* ✅ Correct answer identification
* 💡 Answer explanations
* 🔢 Configurable number of questions
* 📦 Clean JSON output (machine-readable)
* 🖥️ Simple and intuitive UI

---

## 🏗️ Architecture Overview

```
Frontend (Streamlit UI)
        ↓
Text / PDF Input
        ↓
Prompt Engineering + LLM
        ↓
Structured JSON Output (Pydantic)
        ↓
MCQ Display & Evaluation
```

The application is built with **clear frontend–backend separation**, following industry best practices.

---

## 🛠️ Tech Stack

| Layer             | Technology                  |
| ----------------- | --------------------------- |
| Frontend          | Streamlit                   |
| Backend           | Python                      |
| LLM Framework     | LangChain (v1.x)            |
| LLM Provider      | OpenAI / Groq / HuggingFace |
| Output Validation | Pydantic                    |
| File Parsing      | pdfplumber                  |

---

## 📁 Project Structure

The project follows a **simple and clean structure**, keeping all core logic inside a single backend package and a single frontend entry point.

```
mcq-generator/
│
├── src/
│   └── mcqgenerator/            # Backend package (core logic)
│       ├── __init__.py          # Package initializer
│       ├── utils.py             # Helper utilities (JSON handling, validation)
│       ├── prompt.py            # Prompt templates for MCQ generation
│       └── generator.py         # Core MCQ generation logic (LLM calls)
│
├── StreamlitApp.py              # Frontend: Streamlit UI (entry point)
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (API keys)
├── README.md                    # Project documentation
```
