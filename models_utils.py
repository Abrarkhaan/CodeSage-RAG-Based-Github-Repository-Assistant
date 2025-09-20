from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_embedder():
    # Load CodeBERT model from HuggingFace for Embeddings
    bert_model = HuggingFaceEmbeddings(
        model_name="microsoft/codebert-base"
    )
    return bert_model

def load_llm(batch_size: int = 10, max_new_tokens: int = 512):
    # Load HuggingFace pipeline (LLM)
    generator = pipeline(
        "text-generation",
        model="context-labs/meta-llama-Llama-3.2-3B-Instruct-FP16",
        batch_size=batch_size,
        device_map="auto",
        torch_dtype="auto",
        max_new_tokens=max_new_tokens,
        pad_token_id=None,  # will set below
    )
    
    # Ensure pad_token_id is set to eos_token_id if missing
    if generator.tokenizer.pad_token_id is None:
        generator.tokenizer.pad_token_id = generator.tokenizer.eos_token_id
    
    llm = HuggingFacePipeline(pipeline=generator)
    return llm