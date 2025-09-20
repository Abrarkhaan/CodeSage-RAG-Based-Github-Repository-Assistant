import os
import shutil
from langchain_community.vectorstores import FAISS

def build_faiss_index(
    embed_model,
    chunked_docs: list, 
    persist_dir: str = "./faiss_index"
) -> FAISS:
    """
    Build a FAISS vector database from chunked documents using CodeBERT embeddings.

    Args:
        chunked_docs (list): List of LangChain Document chunks.
        persist_dir (str): Directory to store FAISS index.

    Returns:
        FAISS: A FAISS vector store object.
    """
    # Create FAISS index from documents
    vectorstore = FAISS.from_documents(chunked_docs, embed_model)

    # Persist FAISS index
    if os.path.exists(persist_dir): 
        shutil.rmtree(persist_dir)
    os.makedirs(persist_dir, exist_ok=True)
    vectorstore.save_local(persist_dir)

    print(f"FAISS index created and saved at: {persist_dir}")
    return vectorstore

def query_search(query: str, vectorstore, k: int = 5) -> list:
    """
    Search the FAISS vectorstore for the most relevant documents with similarity scores.

    Args:
        query (str): User's search query.
        vectorstore (FAISS): The loaded FAISS vectorstore.
        k (int): Number of top results to return (default = 5).

    Returns:
        List[Tuple[Document, float]]: Top-k matching documents with scores.
    """
    results = vectorstore.similarity_search_with_score(query, k=k)

    if len(results) == 0 or results[0][1] > 50:  # higher score = less similar
        print("Unable to find matching results.")
        return None

    results = sorted(results, key=lambda x: x[1])
    print(f"Top {k} matches for query: '{query}'\n")

    return results