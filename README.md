# 📘 Literature Review Assistant

A clean and lightweight Streamlit app that helps you **generate literature reviews** using papers from **arXiv** and AI-powered analysis.

---

## 🎯 Objective
The main objective of this project is to **simplify and speed up the research process** by automatically gathering, summarizing, and reviewing academic papers. It helps researchers and students quickly identify key ideas, limitations, and future scopes of research without spending hours reading multiple papers.

This project is especially useful for:
- 🎓 **Students** preparing thesis or coursework literature reviews.
- 🧑‍🔬 **Researchers** exploring new topics and identifying research gaps.
- 🧭 **Educators** who need concise summaries for teaching or references.

---

## 🌟 Features
- 🔍 Fetches recent papers from **arXiv** based on your topic.
- 🧠 Uses AI agents to **summarize and critique** research papers.
- 💬 Streams the generated review live in an interactive **Streamlit UI**.
- ⚙️ Works with **Groq** or **OpenAI-compatible** APIs.
- ⏱️ Saves time by highlighting **limitations** and **future enhancement areas** automatically.

---

## 🗂️ Project Structure
```
├── autogen_backend.py     # Core backend logic
├── streamlit_app.py       # Streamlit user interface
├── requirements.txt       # Dependencies
├── .env.example           # Example environment variables
└── README.md              # Project overview
```

---

## 🚀 Getting Started
### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd literature-review-assistant
```

### 2. Set Up the Environment
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API Key
Create a `.env` file in the root folder and add:
```env
GROQ_API_KEY="your_api_key_here"
```

### 4. Run the App
```bash
streamlit run streamlit_app.py
```
Then open the link shown in your terminal (usually `http://localhost:8501`).

---

## 💡 How It Works
1. You enter a research topic (e.g., *Graph Neural Networks*).
2. The backend fetches recent papers from **arXiv**.
3. AI agents (Research Assistant + Reviewer) analyze and summarize key points.
4. The app identifies **limitations** and **future research opportunities** in the papers.
5. The complete review is streamed to the **Streamlit interface** in real time.

---

## 🧾 Requirements
- Python 3.10+
- Main libraries:
  - `streamlit`
  - `arxiv`
  - `autogen-agentchat`
  - `openai`
  - `python-dotenv`

Install all dependencies easily with:
```bash
pip install -r requirements.txt
```

---

## 🚧 Limitations
While powerful, the app currently has a few limitations:
- Depends only on **arXiv** as the paper source (no Semantic Scholar or PubMed yet).
- Generated reviews depend on **LLM quality** and may need human refinement.
- Does not yet support **PDF downloads or offline summaries**.

---

## 🛠️ Future Enhancements
- Add more data sources (Semantic Scholar, PubMed, etc.)
- Export generated reviews as **PDF or Markdown**.
- Provide **keyword filtering** and **paper ranking** by relevance.
- Add **citation formatting** and **bibliography generation**.
- Include an option to **compare research trends** over time.

---

## 📜 License
This project is released under the **MIT License** © 2025.

---

✨ *Built for researchers, students, and lifelong learners — helping you find insights, limitations, and future scopes in minutes instead of hours.*
