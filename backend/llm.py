import os
from dotenv import load_dotenv
import google.generativeai as genai


# Load environment variables
load_dotenv()


# Configure Gemini API
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(context, question):

    prompt = f"""
You are an AI assistant.

Answer the question using only the provided context.

If the answer is not present in the context,
say:
"I could not find this information in the document."


Context:

{context}


Question:

{question}


Answer:
"""


    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )


    response = model.generate_content(
        prompt
    )


    return response.text