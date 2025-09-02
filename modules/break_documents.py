from langchain_text_splitters import RecursiveCharacterTextSplitter

def breakDocument(documentos):

    split = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
         add_start_index=True,


    )
    chunk = split.split_documents(documentos)
    return chunk
    