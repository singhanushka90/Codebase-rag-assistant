<h1 align="center">🧠 CodeBase Intelligence</h1>
<p align="center">AI-Powered Codebase Understanding & Chat System</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-RAG%20Pipeline-121212?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Groq-LLM%20Powered-F55036?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ChromaDB-Vector%20Store-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Deployable-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge" />
</p>

<br/>

---

## 🧠 What Is This?

**CodeBase Intelligence** is an AI-powered developer tool that allows you to **chat with your entire Python codebase** using natural language. Built on a production-grade **Hybrid RAG pipeline** combining Dense Vector Search and BM25 Sparse Retrieval, it enables developers to instantly understand, navigate, and query large codebases without manually reading every file.

> 💡 **Real-World Use Cases:**
> Code Onboarding • Legacy Code Understanding • Team Knowledge Sharing • Automated Code Documentation • AI-Powered Code Review

---

## ⚙️ System Architecture

```
Python Codebase (.py files)
        ↓
DirectoryLoader + TextLoader
        ↓
RecursiveCharacterTextSplitter (Python-aware)
        ↓
HuggingFace Embeddings (all-MiniLM-L6-v2)
        ↓
┌─────────────────────────────┐
│      Hybrid Retrieval       │
│  Dense (Chroma) + BM25      │
│  EnsembleRetriever [0.5,0.5]│
└─────────────────────────────┘
        ↓
Groq LLM (llama3-70b-8192)
        ↓
RunnableWithMessageHistory
        ↓
Chat Response + Memory
```

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📂 **Full Codebase Loading** | Recursively loads all `.py` files |
| 🔍 **Hybrid Search** | Dense + BM25 for maximum retrieval accuracy |
| 🧠 **AI Understanding** | Senior Engineer persona for accurate answers |
| 💬 **Conversational Memory** | Session-based chat history |
| ⚡ **Groq LLM** | Ultra-fast inference |
| 🗃️ **ChromaDB** | Persistent vector storage |
| 🌐 **Streamlit UI** | Clean, developer-friendly interface |

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,streamlit" />
</p>

| Library | Purpose |
|---------|---------|
| **LangChain** | RAG pipeline orchestration |
| **Groq** | Ultra-fast LLM inference |
| **ChromaDB** | Vector database (persistent) |
| **HuggingFace** | `all-MiniLM-L6-v2` embeddings |
| **BM25Retriever** | Sparse keyword retrieval |
| **EnsembleRetriever** | Hybrid search fusion |
| **Streamlit** | Web UI |

---

## 📁 Project Structure

```
CodeBase AI
│
├── 🐍 codebase.py          ← Main Streamlit app
├── 📋 requirements.txt     ← Dependencies
├── 📖 README.md
│
└── 📂 codebase/            ← Your Python files
    ├── module1.py
    ├── module2.py
    └── ...
```

---

## 🚀 Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/singhanushka90/codebase-intelligence.git
cd codebase-intelligence

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Python files
# Place your .py files inside the /codebase folder

# 5. Run the app
streamlit run codebase.py
```

---

## 💻 How To Use

```
1. Enter your Groq API Key in sidebar
2. Click "Load Codebase" button
3. Wait for indexing to complete
4. Ask questions about your code!
```

**Example Questions:**
```
→ "What does the load_policy function do?"
→ "Which files handle authentication?"
→ "Explain the RAG pipeline in app.py"
→ "What libraries are being used?"
→ "Find all functions related to database"
```

---

## 🔍 How Hybrid Search Works

```
Your Question
      ↓
┌─────────────┬──────────────┐
│Dense Search │ BM25 Search  │
│(Semantic)   │ (Keyword)    │
│   50%       │    50%       │
└─────────────┴──────────────┘
              ↓
    EnsembleRetriever
    Best of Both! ✅
              ↓
         Groq LLM
              ↓
      Your Answer 🎯
```

---

## ⚠️ Known Limitations

- Only supports `.py` files currently
- Large codebases may take longer to index
- Requires active internet for Groq API

---

## 🔮 Future Enhancements

| Feature | Description |
|---------|-------------|
| 🌐 **Multi-language** | Support JS, TS, Java, C++ |
| 📄 **GitHub Integration** | Load repos directly from URL |
| 🗺️ **Code Graph** | Visual dependency mapping |
| 🔐 **Local LLM** | Ollama integration for privacy |
| 📊 **Code Analytics** | Complexity & quality metrics |

---

## 👩‍💻 Author

<p align="center">
  <b>Anushka Singh</b><br/>
  B.Tech AI/ML Student | LLM Engineer in Progress<br/>
  <a href="https://github.com/singhanushka90">GitHub: singhanushka90</a>
</p>

---

<p align="center">
  <i>"Making codebases conversational through the power of RAG and LLMs."</i>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,100:0f0c29&height=100&section=footer" />
</p>
