from langchain_community.embeddings import HuggingFaceEmbeddings



def create_embeddings(chunks):


    embeddings = HuggingFaceEmbeddings(

        model_name="sentence-transformers/all-MiniLM-L6-v2"

    )


    vectors = embeddings.embed_documents(chunks)


    return vectors