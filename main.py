import streamlit as st
from repo_loader import load_github_repo
from doc_processing import chunk_documents
from models_utils import load_embedder, load_llm
from vectorstore_utils import build_faiss_index, query_search
from prompt_templates import prompt_template
from response_generator import generate_answer

def main():
    # ---------------- Streamlit App ---------------- #
    st.markdown("<h1 style='text-align: center;'>CodeSage</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: gray;'>RAG-based GitHub CodeBase Assistant</h3>", unsafe_allow_html=True)

    # Initialize session state variables
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None
    if "repo_loaded" not in st.session_state:
        st.session_state.repo_loaded = False

    # bert_model = None

    if "bert_model" not in st.session_state:
        st.session_state.bert_model = None
    if "llm" not in st.session_state:
        st.session_state.llm = None
        
    # Input repo URL or local path
    repo_input = st.text_input("Enter GitHub repository URL or local path:")

    if repo_input:
        if st.button("Process Repository"):
            with st.spinner("Cloning and processing repository..."):
                # Call your repo loading + chunking + FAISS indexing functions here
                docs = load_github_repo(repo_input)
                chunks = chunk_documents(docs, chunk_size=3000, chunk_overlap=1000)
                
                # if bert_model == None:
                #     bert_model = load_embedder()
                #     llm = load_llm(batch_size = 10, max_new_tokens = 512)
                    
                if st.session_state.bert_model is None:
                    st.session_state.bert_model = load_embedder()
                    st.session_state.llm = load_llm(batch_size=10, max_new_tokens=512)
                    
                st.session_state.vectorstore = build_faiss_index(
                    embed_model = st.session_state.bert_model,
                    chunked_docs=chunks, persist_dir="./faiss_index"
                )
                st.session_state.repo_loaded = True
            st.success("Repository processed successfully! You can now ask questions.")

    # User query
    if st.session_state.repo_loaded:
        query = st.text_input("Ask a question about the Repository:")
        if query and st.button("Get Answer"):
            with st.spinner("Searching and generating answer..."):
                # Search in FAISS
                results = query_search(query, st.session_state.vectorstore, k=10)

                # Prepare context + prompt
                context_text = "\n".join([doc.page_content for doc, _ in results])
                # prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
                prompt = prompt_template.format(context=context_text, question=query)

                # Call LLM
                answer = generate_answer(prompt, results, llm=st.session_state.llm)

                # Split answer into Answer + Sources
                if "### Sources:\n" in answer:
                    answer_text, sources_text = answer.split("### Sources:\n", 1)
                else:
                    answer_text, sources_text = answer, "No sources available."

            # Display results
            st.subheader("Answer")
            st.write(answer_text.strip())

            st.subheader("Sources")
            st.write(sources_text.strip())
            
if __name__ == "__main__":
    main()