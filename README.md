# 🤖 AI Research Agent using LangGraph + Flask

An AI-powered Research Agent that answers research questions by searching the web, fetching relevant webpages, summarizing information, and providing source citations.

## 📌 Features

- 🔍 Web Search Tool (DDGS)
- 🌐 Webpage Fetch Tool (Requests + BeautifulSoup)
- 🧠 Summarization Tool
- 📚 Source Citations for every answer
- ⚙️ LangGraph State Machine
- 🛑 Hard Step Limit (Prevents Infinite Loops)
- 🎨 Modern Flask Web Interface (HTML + CSS + JavaScript)
- 📋 Copy Summary Button
- 🕒 Research Timestamp
- 📜 Recent Search History

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| LangGraph | Agent Workflow |
| DDGS | Web Search |
| Requests | Fetch Webpages |
| BeautifulSoup | Extract Page Content |
| HTML/CSS/JavaScript | Frontend |

---

## 📂 Project Structure

research-agent/
│
├── app.py
├── graph.py
├── state.py
├── tools.py
├── requirements.txt
│
├── templates/
│ └── index.html
│
├── static/
│ ├── style.css
│ └── script.js
│
└── README.md

---

## 🚀 How It Works

1. User enters a research question.
2. LangGraph starts the workflow.
3. Search Tool finds relevant webpages.
4. Fetch Tool downloads webpage content.
5. Summarizer creates a concise research summary.
6. Final answer is displayed with source links.

---

## 🔄 LangGraph Workflow

User Question
↓
Search Tool
↓
Fetch Tool
↓
Summarizer
↓
Final Answer + Sources

---

## ▶️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/research-agent.git
cd research-agent

2. Install Dependencies
pip install -r requirements.txt

3. Run the Project
python app.py

Open in browser:

http://127.0.0.1:5000
