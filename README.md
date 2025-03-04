
---

# PDF RAG Chatbot

A chatbot that allows users to upload PDFs and query their content using a Retrieval-Augmented Generation (RAG) approach. This project is designed for **local use** and does not require Docker.

---

## 📋 Features

- **PDF Upload**: Users can upload PDF files.
- **Question Answering**: The chatbot answers questions based on the content of the uploaded PDF.
- **RAG Pipeline**: Uses Retrieval-Augmented Generation for accurate and context-aware responses.
- **Scalable**: Efficiently handles large documents using FAISS for vector search.

---

## 🛠 Tools & Technologies

- **Text Extraction**: `PyMuPDF`
- **Text Splitting**: `LangChain`
- **Embeddings**: `from langchain_ollama import OllamaEmbeddings`
- **Vector Store**: `Chroma Database`
- **LLM**: Ollama `deepseek-r1:8b` for local use

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12
- [pip](https://pip.pypa.io/en/stable/installation/)

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IshanRai9/PDF-RAG-Chatbot
   cd PDF-RAG-Chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -U langchain-community
   pip install -qU "langchain-chroma>=0.1.2"
   pip install -qU langchain-ollama
   ```

3. Add your pdf in data/:
   - Add any pdf in the data/ directory

---

4. Install Ollama:
   - https://ollama.com/
   - Start Ollama if not started and pull the model to use (Deepseek-r1 in my case):
   ```bash
   ollama serve
   ollama pull deepseek-r1:8b
   ```
### Running the Application

1. Vectorize the pdf in the database:
    ```bash
   python populate_database.py
   ```

2. Start the chatbot:
   ```bash
   python query_data.py "Your Query"
   ```

---

## 🧩 How It Works

1. **PDF Upload**: Users upload a PDF file in the data/ directory.
2. **Text Extraction**: Once the populate_database.py is running, the text is extracted from the PDF using `PyMuPDF`.
3. **Chunking**: The loaded documents are split into smaller chunks using RecursiveCharacterTextSplitter. Each chunk is 800 characters long with an 80-character overlap.
4. **Chroma Database Integration:**:The script interacts with a Chroma database to store the document chunks.
Each chunk is converted into a vector and assigned an unique ID based on the source file, page number, and chunk index.
Only new chunks (those not already in the database) are added to the database.
5. **Query Handling**:
   - The user's question is embedded into a vector.
   - Relevant chunks are retrieved from the chroma database.
   - The LLM generates an answer using the retrieved context.
   <img src="https://media.discordapp.net/attachments/856532129381613578/1346420408487772191/Screenshot_53.png?ex=67c81f38&is=67c6cdb8&hm=13d281abcd38845b74812e784d30777852e2761699f95c7018220eccaa5735ea&=&format=webp&quality=lossless" alt="flowchart">
---

## 📂 Project Structure

```
pdf-rag-chatbot/
│   query_data.py               # Main application which accepts query
│   populate_database.py        # PDF processing and RAG pipeline
│   get_embedding_function.py   # Model Embedding
├── tests_rag.py                # Unit tests
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🧪 Testing

To run unit tests:
```bash
pytest test_rag.py
```

---

## 🚨 Troubleshooting

### 1. **Ollama Not Dowloaded**
   - Make sure to have Ollama downloaded and a LLM pulled according to the code.
   - Download Ollama: https://ollama.com/
   -After Downloading:
   ```bash
   ollama serve
   ollama pull mistral
   ```
   - Mistral model is the one I have used, pull and change the code according to your needs.

### 2. **Missing Dependencies**
   - Ensure all dependencies are installed:
     ```bash
     pip install -r requirements.txt
     ```

### 3. **No pdfs**
   - Make sure to have a pdf in data directory and run populate_database.py to vectorize it.w

---

## 📈 Future Improvements

- Run non locally using API Key like OpenAI API
- Add support for other document formats (e.g., Word, CSV).
- Implement hybrid search (keyword + vector).
- Add document history.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [LangChain](https://www.langchain.com/) for the RAG pipeline.
- [Ollama](https://ollama.com/) for the LLMs.
- [Mistral](https://ollama.com/library/mistral) for the Mistral model.

---

## 📧 Contact

For questions or feedback, reach out to:
- **Ishan Rai**  
- **Email**: ishanrai1109@gmail.com  
- **GitHub**: [IshanRai9](https://github.com/IshanRai9)

---
