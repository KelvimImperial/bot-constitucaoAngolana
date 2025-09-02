from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
funcao_embedding = OpenAIEmbeddings()

def createDB(chunk):

    db = Chroma.from_documents(chunk,embedding=funcao_embedding,persist_directory="./db")
    print("Base De Dados Criado Com Sucesso")