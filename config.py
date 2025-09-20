CHUNK_SIZE = 3000
CHUNK_OVERLAP = 1000
FAISS_DIR = "./faiss_index"
BERT_MODEL = HuggingFaceEmbeddings(model_name="microsoft/codebert-base")
LLM_MODEL = "context-labs/meta-llama-Llama-3.2-3B-Instruct-FP16"