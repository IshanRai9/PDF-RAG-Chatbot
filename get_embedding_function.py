from langchain_ollama import OllamaEmbeddings

#I will be using deepseek-r1 from Ollama,.
def get_embedding_function():
    embeddings = OllamaEmbeddings(model="deepseek-r1:8b",)
    return embeddings