import os

import ollama
import faiss
import numpy as np
from dotenv import load_dotenv
from pypdf import PdfReader

# -------------------------------
# LOAD ENV VARIABLES
# -------------------------------

load_dotenv()

# Models
LLM_MODEL = os.getenv("LLM_MODEL")
EMBED_MODEL = os.getenv("EMBED_MODEL")

# Retrieval
TOP_K = int(os.getenv("TOP_K"))
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD"))

# Chunking
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))


# -------------------------------
# 1. DATA INGESTION
# -------------------------------

def load_pdfs(uploaded_files):

    text = ""

    for pdf in uploaded_files:

        reader = PdfReader(pdf)

        for page in reader.pages:

            content = page.extract_text()

            if content:
                text += content + "\n"

    return text


# -------------------------------
# 2. CHUNKING
# -------------------------------

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):

    chunks = []

    for i in range(0, len(text), chunk_size - overlap):

        chunks.append(text[i:i + chunk_size])

    return chunks


# -------------------------------
# 3. EMBEDDING
# -------------------------------

def get_embedding(text):

    response = ollama.embed(
        model=EMBED_MODEL,
        input=text
    )

    return response["embeddings"][0]


# -------------------------------
# 4. VECTOR DATABASE (FAISS)
# -------------------------------

def create_vector_db(chunks):

    embeddings = []

    for chunk in chunks:
        embeddings.append(get_embedding(chunk))

    embeddings = np.array(embeddings, dtype="float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


# -------------------------------
# 5. RETRIEVAL
# -------------------------------

def retrieve(query, index, chunks):

    query_embedding = np.array(
        [get_embedding(query)],
        dtype="float32"
    )

    distances, indices = index.search(query_embedding, TOP_K)

    # Reject unrelated questions
    if distances[0][0] > SIMILARITY_THRESHOLD:
        return None

    retrieved_text = ""

    for i in indices[0]:
        retrieved_text += chunks[i] + "\n\n"

    return retrieved_text


# -------------------------------
# 6. AUGMENT + GENERATE
# -------------------------------

def ask_question(query, index, chunks):

    context = retrieve(query, index, chunks)

    if context is None:
        return "I couldn't find this information in the uploaded PDFs."

    prompt = f"""
You are a precise AI Study Assistant.

Answer ONLY from the provided context.

Rules:
1. If the answer is present in the context, answer it.
2. If the answer is NOT present, reply exactly:
   "I don't have information about this in the provided documents."
3. Never use outside knowledge.
4. Be concise.
5. Use bullet points whenever appropriate.

Context:
{context}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
