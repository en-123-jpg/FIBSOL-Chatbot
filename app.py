from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import os

load_dotenv()

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector DB if not already present
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

# LLM
llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

def run_agent(query):

    # Normalize query
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

    # Retrieve more relevant chunks
    docs = vectordb.similarity_search(query, k=5)

    context = "\n".join([doc.page_content for doc in docs])

    # Better prompt
    prompt = f"""
You are an AI assistant for a biofertilizer company.

Answer ONLY using the provided context.

Guidelines:
- Give detailed and informative answers
- Explain products, benefits, and applications clearly
- Use bullet points for readability
- Mention dosage, microbes, and application methods whenever available
- If recommending a product, explain why it is suitable
- Maintain a professional and natural tone
- Avoid cheesy, overly emotional, or exaggerated phrases
- Do NOT invent information outside the context

If the answer is unavailable, say:
"I’m not sure about that yet, but I can help with product and crop-related questions."

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.content
