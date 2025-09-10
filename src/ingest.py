import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

load_dotenv()

for key in ("GOOGLE_API_KEY", "OPENAI_API_KEY", "DATABASE_URL", "PGVECTOR_COLLECTION_NAME", "PDF_PATH"):
    if not os.getenv(key):
        raise RuntimeError(f"Environment variable {key} is not set.")

PDF_PATH = os.getenv("PDF_PATH")

embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("GEMINI_EMBEDDING_MODEL", "models/gemini-embedding-001"))  # type: ignore
pgvector_store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION_NAME"),
    connection=os.getenv("DATABASE_URL"),
    use_jsonb=True
)

def ingest_pdf():
    docs = PyPDFLoader(str(PDF_PATH)).load()
    print(f"Loaded {len(docs)} documents from {PDF_PATH}")

    splits = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        add_start_index=False,
    ).split_documents(docs)
    print(f"Split into {len(splits)} chunks.")

    enriched_docs = [
        Document(
            page_content=doc.page_content,
            metadata={
                key: value for key, value in doc.metadata.items() if value not in ("", None)
            },
        )
        for doc in splits
    ]

    doc_ids = [f"doc-{i}" for i in range(len(enriched_docs))]

    pgvector_store.add_documents(documents=enriched_docs, ids=doc_ids)

if __name__ == "__main__":
    ingest_pdf()
