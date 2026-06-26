print("🚀 FastAPI starting - lightweight mode")

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os
import traceback
# IMPORTANT: avoid heavy imports at startup where possible
from pdf_loader import extract_text
from text_splitter import split_text

# vector store will be used lazily inside endpoints
# from vector_store import create_vector_store, load_vector_store
from llm import ask_gemini

app = FastAPI(debug=True)
# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://ai-pdf-qa.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- FOLDERS ----------------
os.makedirs("uploads", exist_ok=True)

# ---------------- REQUEST MODEL ----------------
class ChatRequest(BaseModel):
    question: str


# ---------------- ROOT ----------------
@app.get("/")
def home():
    return {"message": "AI PDF Q&A Running 🚀"}


# ---------------- UPLOAD PDF ----------------
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    try:
        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        text = extract_text(file_path)

        chunks = split_text(text)

        from vector_store import create_vector_store

        create_vector_store(chunks)

        return {
            "filename": file.filename,
            "chunks": len(chunks),
            "message": "PDF processed successfully"
        }

    except Exception as e:
        traceback.print_exc()
        return {
            "error": str(e)
        }

# ---------------- CHAT ----------------
@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        # ⚡ LAZY IMPORT (VERY IMPORTANT for Render memory)
        from vector_store import load_vector_store

        vector_db = load_vector_store()

        if vector_db is None:
            return {"error": "Please upload PDF first"}

        # Similarity search (limit k = lower memory + faster)
        docs = vector_db.similarity_search(req.question, k=2)

        # Build context (keep small for token + memory efficiency)
        context = "\n".join([doc.page_content for doc in docs])

        # Ask Gemini
        answer = ask_gemini(context, req.question)

        return {
            "question": req.question,
            "answer": answer
        }
    except Exception as e:
        traceback.print_exc()
        return {
            "error": str(e)
        }
