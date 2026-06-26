import os
from dotenv import load_dotenv
import google.generativeai as genai


# Load .env file
load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")


if not api_key:
    raise Exception("GEMINI_API_KEY missing")


genai.configure(
    api_key=api_key
)


def ask_gemini(context, question):

    prompt = f"""
You are an AI assistant.

Answer only from the document context.

If answer is not present:
"I could not find this information in the document."


Context:

{context}


Question:

{question}


Answer:
"""


    model = genai.GenerativeModel(
        "gemini-1.5-flash"
    )


    response = model.generate_content(prompt)


    return response.text