🧠 MCQ Generator

An AI-powered MCQ Generator that automatically creates multiple-choice questions from input text using Large Language Models (LLMs).
Built with Python and Streamlit, the app generates structured, validated JSON output suitable for quizzes, exams, and e-learning platforms.

🚀 Features

📄 Generate MCQs from any input text

🤖 LLM-powered question generation

🎯 Adjustable difficulty levels

📊 Structured JSON output

🧪 Built-in JSON validation & error handling

🌐 Interactive Streamlit UI

🛠️ Tech Stack

Python 3.9+

Streamlit

LangChain

LLMs (OpenAI / Groq / HuggingFace – configurable)

JSON

📂 Project Structure
mcq-generator/
│
├── src/
│   └── mcqgenerator/
│       ├── utils.py
│       ├── prompt.py
│       └── generator.py
│
├── StreamlitApp.py
├── requirements.txt
├── README.md
└── .env

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/mcq-generator.git
cd mcq-generator

2️⃣ Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

🔐 Environment Variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_api_key_here


(Or Groq / HuggingFace keys if used)

▶️ Run the Application
streamlit run StreamlitApp.py


The app will open in your browser at:

http://localhost:8501

🧪 Sample Output (JSON)
{
  "quiz": [
    {
      "question": "What is Machine Learning?",
      "options": ["AI technique", "Programming language", "Database", "OS"],
      "correct": "AI technique"
    }
  ]
}

⚠️ Common Issues

Invalid JSON output
Ensure the LLM prompt enforces strict JSON format

JSONDecodeError
Remove extra text or markdown before parsing:

data = data.strip().replace("```json", "").replace("```", "")

🌟 Future Improvements

Export MCQs to PDF / CSV

User authentication

Question tagging & topic-wise generation

Database integration

Multi-language support

🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Vinaykumar Yadav
Engineering Student | AI & Python Enthusiast
