# 📂 CodeSage - RAG-based GitHub CodeBase Assistant

**Tagline:** *AI-powered assistant for exploring and understanding any
codebase.*

------------------------------------------------------------------------

## 🚀 Overview

CodeSage is a Retrieval-Augmented Generation (RAG) powered assistant
designed to help developers **explore, understand, and query any GitHub
repository** with natural language.

It combines:

-   **LangChain** – Handles repository parsing, splitting files into manageable text chunks for retrieval, and the RAG pipeline.
-   **FAISS** – Efficiently stores and searches the vector embeddings of code/document chunks to retrieve the most relevant context.
-   **HuggingFace CodeBERT** – Generates high-quality embeddings for code and documentation, enabling semantic similarity search.
-   **HuggingFace LLaMA 3.2-3B** – Acts as the reasoning engine to generate natural language answers grounded in the retrieved context.
-   **Streamlit** – Provides a simple web interface for uploading repositories, asking questions, and viewing structured answers with sources.

------------------------------------------------------------------------

## ✨ Features

-   Clone or load any GitHub repository
-   Automatically index code files, documentation, and configs
-   Ask natural language questions about the repo
-   Retrieve **contextual answers** with **source file references**
-   Supports **Markdown rendering** and code snippets

------------------------------------------------------------------------

## 🖥️ Demo Screenshots

### 🔹 Streamlit Interface

<img width="1364" height="590" alt="1" src="https://github.com/user-attachments/assets/b83f76aa-f994-4dad-8063-eb1488f41567" />
<img width="1347" height="587" alt="2" src="https://github.com/user-attachments/assets/d25bc061-b2e8-4880-af8d-00ae96dfbbc3" />
<img width="1358" height="596" alt="3" src="https://github.com/user-attachments/assets/8318cedb-4b9e-4304-af22-efcabfd56449" />

### 🔹 Conversation Example

<img width="1352" height="532" alt="0001" src="https://github.com/user-attachments/assets/f66c3a3b-14b1-4c90-81f0-b10ac283433e" />
<img width="1345" height="549" alt="001" src="https://github.com/user-attachments/assets/be3dddd0-beb8-44d2-9499-4f3018e275a2" />
<img width="1347" height="582" alt="4" src="https://github.com/user-attachments/assets/e2a12ebc-fde4-4081-9a6b-0bee4e8af0e2" />
<img width="1343" height="583" alt="5" src="https://github.com/user-attachments/assets/5d30dcbf-dd6c-46b8-8a14-aec047c7a521" />
<img width="1350" height="585" alt="6" src="https://github.com/user-attachments/assets/ffcf13bd-cb9e-471e-a927-c18874069f1f" />
<img width="1324" height="582" alt="7" src="https://github.com/user-attachments/assets/6c6fd1d3-01a7-4381-8ac5-4f4b894be671" />
<img width="1341" height="586" alt="8" src="https://github.com/user-attachments/assets/82222395-bdaf-41ba-ab5a-6a1fc7ee7d5f" />
<img width="1334" height="564" alt="9" src="https://github.com/user-attachments/assets/54203558-7ea1-4c80-ae1c-aad09e9f5fbb" />
<img width="1345" height="581" alt="10" src="https://github.com/user-attachments/assets/4c26bc92-29f3-40ea-a8f0-5b541428c8f6" />
<img width="1343" height="588" alt="11" src="https://github.com/user-attachments/assets/8f25d82c-5eac-41d8-81b9-149b4fd89fe9" />
<img width="1332" height="576" alt="12" src="https://github.com/user-attachments/assets/890a69ae-12ce-48cd-921c-0c0bf4c57958" />
<img width="1341" height="576" alt="13" src="https://github.com/user-attachments/assets/1fabd28d-7dc5-4442-adab-3a351d05b26f" />
<img width="1340" height="560" alt="14" src="https://github.com/user-attachments/assets/ec6d5ca0-beae-47a9-8aa6-f4b6c0c47aa3" />
<img width="1351" height="583" alt="15" src="https://github.com/user-attachments/assets/35449468-81a2-4a95-952a-9b4458db3c89" />
<img width="1345" height="581" alt="16" src="https://github.com/user-attachments/assets/e70afe35-91ab-48d4-80f9-804154a51c90" />
<img width="1346" height="442" alt="17" src="https://github.com/user-attachments/assets/b60faeee-4543-4b72-9c92-9e9a25fba3c3" />

------------------------------------------------------------------------

## ⚙️ Installation

### 1. Clone this Repository

``` bash
git clone https://github.com/abrarkhaan/CodeSageCodeSage-RAG-Based-Github-Repository-Assistant.git
cd CodeSageCodeSage-RAG-Based-Github-Repository-Assistant
```

### 2. Create Virtual Environment & Install Dependencies

``` bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Streamlit App

``` bash
streamlit run main.py
```

The app will run at `http://localhost:8501`

------------------------------------------------------------------------

## 🧑‍💻 Usage

1.  Enter a GitHub repository URL or local path.
2.  Wait for CodeSage to **clone, process, and index** the repo.
3.  Ask natural language questions like:
    -   *"Where is the main entry point of this repo?"*
    -   *"How does the model handle multilingual transcription?"*
    -   *"What external libraries does this repo depend on?"*
4.  View the **answer** and **sources** directly in the interface.

------------------------------------------------------------------------

## 📂 Project Structure

    CodeSage/
    │
    ├─ main.py                 # Streamlit UI
    ├─ repo_loader.py         # GitHub repo loading
    ├─ doc_processing.py     # Text splitting & chunking
    ├─ vectorstore_utils.py   # FAISS index creation & search
    ├─ models_utils.py           # LLM loading and calls
    ├─ prompt_templates.py    # Prompt definitions
    ├─ response_generator     # Query Response Generation 
    ├─ config.py              # Configurations & constants
    ├─ requirements.txt       # Dependencies
    └─ README.md              # Project documentation

------------------------------------------------------------------------

## 🧪 Example Questions

-   *"What are the main modules and their responsibilities?"*
-   *"How does this repo handle configuration and error handling?"*
-   *"Where is the model initialized?"*
-   *"Which files explain how to run the example scripts?"*

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **[Streamlit](https://streamlit.io/)** -- UI framework
-   **[LangChain](https://www.langchain.com/)** -- RAG pipeline
-   **[FAISS](https://github.com/facebookresearch/faiss)** -- Vector
    similarity search
-   **[HuggingFace Transformers](https://huggingface.co/transformers/)**
    -- Embeddings + LLMs

------------------------------------------------------------------------

## 🤝 Contributing

Contributions are welcome! Please fork this repo and submit a pull
request.

------------------------------------------------------------------------

## 📜 License

---.

------------------------------------------------------------------------

## 🙌 Acknowledgements

-   [OpenAI Whisper](https://github.com/openai/whisper)
-   [LangChain](https://github.com/hwchase17/langchain)
-   [Streamlit](https://github.com/streamlit/streamlit)
-   [HuggingFace](https://huggingface.co/)

------------------------------------------------------------------------
