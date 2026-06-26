from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os


DB_PATH = "faiss_db"


def get_embeddings():

    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )


def create_vector_store(chunks):

    embeddings = get_embeddings()

    vectordb = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    vectordb.save_local(DB_PATH)

    return vectordb


def load_vector_store():

    if not os.path.exists(DB_PATH):
        return None

    embeddings = get_embeddings()

    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )