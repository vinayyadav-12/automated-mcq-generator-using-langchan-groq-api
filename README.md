# MCQs Creator Application with LangChain 🧠🤖

A **production-ready Large Language Model (LLM) powered application** that automatically generates **high-quality Multiple Choice Questions (MCQs)** from text or PDF input. The system supports **difficulty levels, correct answers, and explanations**, making it suitable for EdTech platforms, exam preparation, and AI portfolios.

---

## 🎯 Problem Statement

Creating quality MCQs manually is time-consuming and requires subject expertise. This project solves that problem by leveraging **LLMs** to automatically generate structured, exam-ready MCQs from learning material.

---

## 🚀 Features

* 📄 Generate MCQs from text or PDF content
* 🎯 Difficulty levels: Easy / Medium / Hard
* 🔢 Configurable number of questions
* ✅ Correct option identification
* 💡 Explanation for each answer
* 📦 Strict JSON-based output (machine readable)
* 🖥️ Simple and intuitive Streamlit UI

---

## 🏗️ Architecture Overview

```
User Input (Text / PDF)
        ↓
Streamlit Frontend
        ↓
MCQ Generator Backend (Python Package)
        ↓
Prompt Engineering + LLM
        ↓
Structured MCQ JSON Output
```

The architecture ensures **clear separation of concerns**, easy debugging, and scalability.

---

## 🛠️ Tech Stack

| Layer             | Technology       |
| ----------------- | ---------------- |
| Frontend          | Streamlit        |
| Backend           | Python           |
| LLM Framework     | LangChain (v1.x) |
| LLM Provider      | OpenAI / Groq    |
| Output Validation | Pydantic         |
| File Parsing      | pdfplumber       |

---

## 📂 Project Structure

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

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-mcq-generator.git
cd ai-mcq-generator
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/binactivate   # Windows: venv\\Scripts\\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

```bash
streamlit run StreamlitApp.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧪 Backend Usage (Without UI)

You can directly use the backend MCQ generator module:

```python
from mcqgenerator.generator import generate_mcqs

text = """
Machine learning is a subset of artificial intelligence that focuses on learning from data.
"""

mcqs = generate_mcqs(text, number=5, difficulty="Medium")
print(mcqs)
```

---

## 📦 Example Output

```json
{
  "question": "What is machine learning?",
  "options": {
    "A": "A type of hardware",
    "B": "A subset of artificial intelligence",
    "C": "A programming language",
    "D": "A database system"
  },
  "correct": "B",
  "explanation": "Machine learning is a field of AI that enables systems to learn from data."
}
```

---

## 🧠 Key Engineering Highlights

* ✅ Prompt-driven MCQ generation
* ✅ Strict JSON schema enforcement
* ✅ LangChain 1.x compatible (`invoke()` based calls)
* ✅ Modular backend packaged for reuse
* ✅ Easy integration with other systems

---

## 🔮 Future Enhancements

* 📊 MCQ evaluation & scoring system
* ⏱️ Timed quizzes
* 🧪 Topic-wise MCQ generation
* 📄 Export MCQs to PDF / CSV
* 🔐 User authentication
* 🌐 REST API using FastAPI

---

## 💼 Use Cases

* Online examination systems
* EdTech platforms
* Coaching institutes
* AI-powered learning tools
* Academic & corporate training

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Author

**Vinaykumar Yadav**
Engineering Student | AI & LLM Developer

---

⭐ If you find this project useful, consider giving it a star!
