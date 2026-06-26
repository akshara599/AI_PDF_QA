from fastapi import FastAPI, UploadFile, File
import shutil


from pdf_loader import extract_text
from text_splitter import split_text
from vector_store import create_vector_store
from llm import ask_gemini
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(

    CORSMiddleware,

    allow_origins=[
           "http://localhost:5173",
            "https://your-frontend-name.vercel.app"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)


vector_db = None



@app.get("/")
def home():

    return {

        "message":"AI PDF Q&A Running"

    }




@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):


    global vector_db



    file_path = f"uploads/{file.filename}"



    with open(file_path,"wb") as buffer:

        shutil.copyfileobj(

            file.file,

            buffer

        )



    text = extract_text(file_path)



    chunks = split_text(text)



    vector_db = create_vector_store(chunks)



    return {


        "filename":file.filename,


        "chunks":len(chunks),


        "message":"PDF processed successfully"

    }





@app.post("/chat")
async def chat(question:str):


    if vector_db is None:

        return {

            "error":"Please upload PDF first"

        }



    docs = vector_db.similarity_search(

        question,

        k=3

    )



    context = ""



    for doc in docs:

        context += doc.page_content + "\n"



    answer = ask_gemini(

        context,

        question

    )



    return {


        "question":question,


        "answer":answer

    }