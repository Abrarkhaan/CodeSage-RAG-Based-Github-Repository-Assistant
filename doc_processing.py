from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(
    docs: list, 
    chunk_size: int = 3000, 
    chunk_overlap: int = 1000
) -> list:
    """
    Split documents into smaller overlapping chunks for embeddings.

    Args:
        docs (list): List of LangChain Document objects.
        chunk_size (int): Max size of each chunk (characters).
        chunk_overlap (int): Overlap between consecutive chunks.

    Returns:
        List[Document]: Chunked documents with preserved metadata.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        add_start_index=True,
        separators=["\n\n", "\n", " ", ""],  # progressively finer splits
    )
    chunked_docs = text_splitter.split_documents(docs)

    print(f"Split {len(docs)} documents into {len(chunked_docs)} chunks "
          f"(avg {len(chunked_docs)//len(docs)} chunks per doc)")
    return chunked_docs