from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

import os

DB_PATH = "chroma_db"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
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