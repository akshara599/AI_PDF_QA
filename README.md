# 🤖 AI PDF Q&A (Chat with PDF)

An AI-powered document question answering system using **RAG (Retrieval Augmented Generation)**.  
Upload a PDF, ask questions, and get answers from your document using Gemini AI.

🌐 Live Demo:
https://ai-pdf-qa-three.vercel.app/

---

## 🚀 Features

- 📄 Upload PDF documents
- 🔍 Semantic search using embeddings
- 🗂️ FAISS vector database
- 🤖 Gemini 2.5 AI responses
- 💬 Ask questions from documents
- ⚡ Fast React + FastAPI application

---

## 🧠 How It Works


PDF Upload
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
FAISS Vector Search
↓
Gemini 2.5
↓
Answer


---

## 🛠️ Tech Stack

### Frontend
- React.js
- Vite
- Axios

### Backend
- Python
- FastAPI
- LangChain

### AI
- Google Gemini 2.5
- HuggingFace Embeddings
- RAG Architecture

### Vector Database
- FAISS

---

## 📂 Project Structure


AI-PDF-QA

├── backend
│ ├── main.py
│ ├── embeddings.py
│ ├── vector_store.py
│ ├── llm.py
│ └── requirements.txt
│
└── frontend
├── src
└── package.json


---

## ⚙️ Run Locally

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload

Create .env

GEMINI_API_KEY=your_api_key
Frontend
cd frontend

npm install

npm run dev
🔌 API
Upload PDF
POST /upload
Ask Question
POST /chat

Example:

{
 "question":"Summarize this document"
}
🔮 Future Improvements
Chat history
Multiple PDF support
Source citations
Authentication
Persistent vector storage

⭐ Built using RAG + Gemini AI