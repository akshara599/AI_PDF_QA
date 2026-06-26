from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

DB_PATH = "chroma_db"

# ✅ THIS IS THE KEY CHANGE (NO LOCAL MODEL)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)


def create_vector_store(chunks):
    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    vectordb.persist()
    return vectordb


def load_vector_store():
    if not os.path.exists(DB_PATH):
        return None

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )