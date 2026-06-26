import os

from dotenv import load_dotenv

from google import genai



# Load environment variables
load_dotenv()



# Create Gemini client
client = genai.Client(

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


    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=prompt

    )


    return response.text