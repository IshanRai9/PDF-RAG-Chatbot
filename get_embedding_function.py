from langchain_ollama import OllamaEmbeddings

#embedding function for the pdf
def get_embedding_function():
    embeddings = OllamaEmbeddings(model="mistral",)
    return embeddings