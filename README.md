# CodeBase Intelligence

AI-powered codebase understanding system built using Hybrid Retrieval-Augmented Generation (RAG).

CodeBase Intelligence enables developers to interact with an entire Python codebase using natural language. Instead of manually navigating files, searching functions, or reading thousands of lines of code, developers can ask questions and receive context-aware answers generated from the actual source code.

---

## Overview

Large codebases are difficult to understand, especially during:

* New developer onboarding
* Legacy system maintenance
* Team handovers
* Feature exploration
* Code reviews

This project solves that problem by combining semantic retrieval, keyword search, conversational memory, and LLM reasoning into a single developer assistant.

---

## Key Capabilities 

### Code Understanding

* Analyze complete Python codebases
* Explain functions, classes, and modules
* Trace implementation logic

### Hybrid Retrieval

* Dense semantic search using embeddings
* Sparse keyword search using BM25
* Ensemble retrieval for improved accuracy

### Conversational AI

* Multi-turn conversations
* Session-based memory
* Context-aware responses

### Developer Productivity

* Faster onboarding
* Reduced documentation dependency
* Instant code exploration

---

## Architecture

```text
Python Files (.py)
        │
        ▼
DirectoryLoader
        │
        ▼
RecursiveCharacterTextSplitter
        │
        ▼
HuggingFace Embeddings
(all-MiniLM-L6-v2)
        │
        ▼
Chroma Vector Database
        │
        ▼
┌─────────────────────────────┐
│      Hybrid Retrieval       │
│                             │
│ Dense Retrieval (Chroma)    │
│           +                 │
│ Sparse Retrieval (BM25)     │
└─────────────────────────────┘
        │
        ▼
EnsembleRetriever
        │
        ▼
Groq LLM
(llama3-70b-8192)
        │
        ▼
Conversational Memory
        │
        ▼
Developer Response
```

---

## Technology Stack

| Component    | Technology                 |
| ------------ | -------------------------- |
| Language     | Python                     |
| Frontend     | Streamlit                  |
| Framework    | LangChain                  |
| LLM          | Groq                       |
| Embeddings   | HuggingFace                |
| Vector Store | ChromaDB                   |
| Retrieval    | BM25 + Dense Retrieval     |
| Memory       | RunnableWithMessageHistory |

---

## Project Structure

```text
codebase-intelligence/
│
├── codebase.py
├── requirements.txt
├── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/singhanushka90/codebase-intelligence.git
cd codebase-intelligence
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Application

```bash
streamlit run codebase.py
```

---

## Example Queries

```text
What does load_policy() do?

Explain the authentication workflow.

Which files are responsible for retrieval?

Show all database-related functions.

How does the RAG pipeline work?

Find classes related to user management.
```

---

## Retrieval Strategy

This project uses a Hybrid Retrieval architecture.

### Dense Retrieval

Captures semantic meaning using vector embeddings.

Example:

Query:
"How is user login implemented?"

Can retrieve:

"authenticate_user()"

even when exact words differ.

### Sparse Retrieval (BM25)

Captures exact keyword matches.

Example:

Query:
"load_policy"

Returns chunks containing that exact function.

### Ensemble Retrieval

Combines both approaches:

```python
EnsembleRetriever(
    retrievers=[dense, sparse],
    weights=[0.5, 0.5]
)
```

Result:
Higher retrieval precision and better answer quality.

---

## Future Roadmap

* JavaScript support
* TypeScript support
* Java support
* GitHub repository ingestion
* Repository-level summarization
* Dependency graph visualization
* Local LLM support via Ollama
* Docker deployment
* Source citation support

---

## Screenshots

Add screenshots here:

```text
screenshots/home.png
screenshots/chat.png
screenshots/retrieval.png
```

---

## Author

Anushka Singh

B.Tech Artificial Intelligence & Machine Learning

Focused on:

* Generative AI
* Retrieval-Augmented Generation
* LLM Engineering
* AI Applications

---

## License

This project is available for educational and research purposes.
