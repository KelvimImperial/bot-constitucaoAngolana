from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma.vectorstores import Chroma
from dotenv import load_dotenv
from langchain.schema import StrOutputParser

load_dotenv()
BD ="./db"

model = ChatOpenAI(model="gpt-4o",temperature=0.1)
funcao_embedding =OpenAIEmbeddings()

parser =StrOutputParser()



db =Chroma(persist_directory=BD,embedding_function=funcao_embedding)

def agentAI(text):
    
  

    pergunta =text

    

    similarity = db.similarity_search_with_relevance_scores(pergunta, k=4)
        
        
    if not similarity or max(score for _, score in similarity) < 0.5:
           
            return "Desculpe, não encontrei informações suficientes."
             
            

       

    texto_resultados = [doc.page_content for doc, score in similarity]
    context = "\n\n----\n\n".join(texto_resultados)
    
        
    prompt_template = ChatPromptTemplate([
        ("system", 
        "Você é um assistente virtual com personalidade humana, especializado em responder perguntas sobre a Constituição da República de Angola. "
        "Regras: "
        "1 - Base Única: Responder apenas com base na Constituição. "
        "2 - Clareza: Linguagem formal, clara e objetiva. "
        "3 - Referência: Sempre citar artigo e número (ex.: Artigo 23.º — Princípio da Igualdade). "
        "4 - Neutralidade: Não emitir opiniões pessoais, apenas explicar, interpretar ou resumir. "
        "5 - Transparência: Se não houver resposta direta, diga: 'A Constituição da República de Angola não trata diretamente desse assunto.' "
        "6 - Citação: Manter fidelidade literal ao texto. "
        "7 - Explicação: Simplificar quando necessário para melhor compreensão. "
        "8 - Omissões: Se não constar, não opinar; indicar a parte mais próxima do tema. "
        "IMPORTANTE: Responda SEM usar asteriscos (*), markdown ou negrito. Apenas texto simples."
        ),
        ("user", 
        "pergunta do usuário: {pergunta}\n"
        "Use APENAS as informações abaixo para responder:\n{context}"
        )
])

    chain = prompt_template | model | parser

    resultado = chain.invoke({"pergunta":pergunta,"context":context})
    return resultado

        


        