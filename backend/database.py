from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()


mongo_url = os.getenv("MONGO_URL")


client = MongoClient(mongo_url)

print("Mongo connected")

db = client["pdf_chat"]

history_collection = db["chat_history"]