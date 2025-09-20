def generate_answer(prompt, results, llm) -> str:
    """
    Generate an answer to the query using LLaMA 3.2-3B-Instruct with RAG context.

    Args:
        prompt (str): Formatted prompt containing context + query.
        results (list): Retrieved documents with scores (from FAISS).
        model_id (str): HuggingFace model ID.

    Returns:
        str: Well-structured answer with sources.
    """

    # Generate answer
    raw_answer = llm(prompt)

    # Collect unique sources from retrieved docs
    # sources = list({doc.metadata.get("source", "unknown") for doc, _ in results})
    sources = list({doc.metadata.get("source", "unknown") for doc, score in results if score < 65})

    # Format final response
    answer = (
        f"### Answer:\n{raw_answer.strip()}\n\n"
        f"---\n\n"
        f"### Sources:\n" + "\n".join(f"- {src}" for src in sources)
    )

    if "Answer:" in answer:
        final_answer = answer.split("Answer:")[-1].strip()
    else:
        final_answer = answer.strip()

    return final_answer