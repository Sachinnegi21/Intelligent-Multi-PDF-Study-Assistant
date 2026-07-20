# 📚 Intelligent Multi-PDF Study Assistant

An AI-powered Study Assistant that allows users to upload multiple PDF documents and interact with them using natural language. The application leverages Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers directly from uploaded study materials, making learning faster and more efficient.

---

## 🚀 Features

- 📄 Upload and process multiple PDF documents
- 🤖 AI-powered question answering
- 🔍 Semantic search using vector embeddings
- 📚 Retrieval-Augmented Generation (RAG)
- 🧠 Context-aware responses from uploaded PDFs
- 💬 Interactive chat interface
- ⚡ Fast document retrieval with FAISS
- 📝 Summarize study materials
- 🎯 Explain complex concepts
- 🔄 Multi-document knowledge retrieval

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Framework
- Streamlit

### AI & LLM
- Ollama
- Llama 3.2

### AI Framework
- LangChain

### Vector Database
- FAISS

### Embeddings
- Ollama Embeddings

### PDF Processing
- PyPDF2
- pypdf

### Other Libraries
- NumPy
- Pandas
- python-dotenv

---

## 🧠 How It Works

1. Upload one or more PDF files.
2. Extract text from each document.
3. Split text into smaller chunks.
4. Generate vector embeddings.
5. Store embeddings in a FAISS vector database.
6. Retrieve relevant chunks using semantic search.
7. Pass retrieved context to the LLM.
8. Generate accurate, document-based answers.

---

## 🏗️ Project Architecture

```
                User
                  │
                  ▼
        Upload Multiple PDFs
                  │
                  ▼
          Text Extraction
                  │
                  ▼
           Text Chunking
                  │
                  ▼
       Ollama Embeddings
                  │
                  ▼
         FAISS Vector Store
                  │
        Semantic Retrieval
                  │
                  ▼
             LangChain
                  │
                  ▼
           Ollama LLM
                  │
                  ▼
          AI Generated Answer
```

---

## 📂 Project Structure

```
Intelligent-Multi-PDF-Study-Assistant/

│── app.py
│── requirements.txt
│── README.md
│── .env
│
├── data/
│      ├── pdfs/
│      └── vector_db/
│
├── utils/
│      ├── pdf_loader.py
│      ├── text_splitter.py
│      ├── embeddings.py
│      ├── vectorstore.py
│      └── rag_chain.py
│
├── assets/
│      └── screenshots/
│
└── models/
```

---

## ✨ Core Functionalities

### 📄 Multi-PDF Upload

Upload multiple study materials simultaneously.

---

### 🔍 Semantic Search

Instead of keyword matching, the application understands the meaning of the question and retrieves the most relevant content.

---

### 🤖 AI Question Answering

Ask questions such as:

- Explain Operating System Scheduling.
- Summarize Chapter 3.
- What is Machine Learning?
- Compare Stack and Queue.
- Give important interview questions.

---

### 📚 RAG Pipeline

The assistant combines:

- Document Retrieval
- Vector Search
- Large Language Models

to produce highly relevant answers.

---

### 💬 Interactive Chat

Users can continue asking follow-up questions while maintaining conversation context.

---

## 💡 Example Questions

- Summarize this chapter.
- Explain this topic in simple language.
- What are the key points?
- Generate important interview questions.
- Create revision notes.
- Explain with examples.
- Compare two concepts.
- What formulas are present?
- Give multiple-choice questions.

---

## 🎯 Skills Demonstrated

- Generative AI
- Retrieval-Augmented Generation (RAG)
- LangChain
- Large Language Models (LLMs)
- AI Agents
- Prompt Engineering
- Vector Databases
- Semantic Search
- Information Retrieval
- PDF Processing
- Natural Language Processing (NLP)
- Streamlit Development
- Python Programming

---

## 🔧 Tools & Technologies

- Python
- Streamlit
- LangChain
- Ollama
- Llama 3.2
- FAISS
- PyPDF2
- pypdf
- Git
- GitHub
- VS Code

---

## 📈 Future Enhancements

- Voice-based question answering
- Flashcard generation
- Quiz generation
- Mind map creation
- Study planner
- OCR support for scanned PDFs
- Citation-aware answers
- Multi-language support
- PDF annotation
- Performance analytics

---

## 🎓 Learning Outcomes

Through this project, I gained hands-on experience with:

- Building RAG applications
- LangChain pipelines
- Vector databases
- Semantic document search
- AI-powered chatbots
- LLM integration using Ollama
- Prompt engineering
- Streamlit application development
- Multi-document retrieval systems

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sachin Negi**

GitHub: https://github.com/Sachinnegi21

If you found this project useful, consider giving it a ⭐ on GitHub!
