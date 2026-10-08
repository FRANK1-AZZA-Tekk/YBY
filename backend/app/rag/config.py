from pydantic_settings import BaseSettings, SettingsConfigDict


class RAGSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    ollama_base_url: str = "http://localhost:11434"
    qdrant_url: str = "http://localhost:6333"
    embedding_model: str = "nomic-embed-text"
    collection_name: str = "yby_knowledge"
    chunk_size: int = 1000
    chunk_overlap: int = 200
    top_k: int = 4


rag_settings = RAGSettings()
