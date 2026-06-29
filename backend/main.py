print("🚀 FastAPI starting - lightweight mode")

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import shutil
import os
import traceback
from datetime import datetime

from pdf_loader import extract_text
from text_splitter import split_text
from database import history_collection
from llm import ask_gemini

# ---------------- APP INIT ----------------
app = FastAPI(debug=True, openapi_version="3.0.2")

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-pdf-qa-three.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- FOLDER ----------------
os.makedirs("uploads", exist_ok=True)

# ---------------- REQUEST MODEL ----------------
class ChatRequest(BaseModel):
    question: str
    user_id: str


# ---------------- ROOT ----------------
@app.get("/")
def home():
    return {"message": "AI PDF Q&A Running 🚀"}


# ---------------- UPLOAD PDF ----------------
@app.post("/upload")
async def upload_pdf(files: List[UploadFile] = File(...)):
    try:
        all_chunks = []

        for file in files:
            file_path = f"uploads/{file.filename}"

            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            text = extract_text(file_path)
            chunks = split_text(text)

            if chunks:
                all_chunks.extend(chunks)

        if not all_chunks:
            raise HTTPException(
                status_code=400,
                detail="No text found in uploaded PDFs"
            )

        # lazy import
        from vector_store import create_vector_store

        create_vector_store(all_chunks)

        return {
            "files_uploaded": len(files),
            "total_chunks": len(all_chunks),
            "message": "Multiple PDFs processed successfully"
        }

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


# ---------------- CHAT ----------------
@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        if not req.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")

        from vector_store import load_vector_store

        vector_db = load_vector_store()

        if vector_db is None:
            raise HTTPException(status_code=400, detail="Please upload PDF first")

        docs = vector_db.similarity_search(
            req.question,
            k=6
        )

        context = "\n".join(doc.page_content for doc in docs)

        answer = ask_gemini(context, req.question)

        history_collection.insert_one({
            "user_id": req.user_id,
            "question": req.question,
            "answer": answer,
            "time": datetime.utcnow()
        })

        return {
            "question": req.question,
            "answer": answer
        }

    except HTTPException as he:
        raise he

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
# ---------------- HISTORY ----------------
@app.get("/history/{user_id}")
def get_history(user_id: str):
    try:
        chats = history_collection.find(
            {"user_id": user_id},
            {"_id": 0}
        )
        return list(chats)

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))