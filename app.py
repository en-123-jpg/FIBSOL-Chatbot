from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import os

load_dotenv()

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create DB if not exists
if not os.path.exists("chroma_db"):

    documents = []

    for file in os.listdir("data"):
        if file.endswith(".pdf"):

            loader = PyPDFLoader(f"data/{file}")
            documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

else:

    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

# Groq model
llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

def run_agent(query):
query = query.lower()

slang_map = {
    "abt": "about",
    "u": "you",
    "ur": "your",
    "wanna": "want to",
    "bio fert": "biofertilizer",
    "prod": "product"
}

for slang, proper in slang_map.items():
    query = query.replace(slang, proper)
    docs = vectordb.similarity_search(query, k=2)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a helpful AI assistant for a biofertilizer company.

Use ONLY the provided context to answer.

If the information is unavailable, politely say:
"I’m not sure about that yet, but I can help with questions related to our products and services."

Context:
{context}

Question:
{query}

Answer in a friendly and professional way.

If the answer is long:
- use bullet points
- keep it readable
- avoid huge paragraphs

Start naturally with:
"I can help with that."
"""

    response = llm.invoke(prompt)

    return response.content
