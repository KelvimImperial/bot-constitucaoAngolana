from langchain_community.document_loaders import  TextLoader


def readingMarkedown():

    carregador = TextLoader("./data/constituicao_republica.md",encoding="utf-8")
    documentos = carregador.load()
    return documentos
   



