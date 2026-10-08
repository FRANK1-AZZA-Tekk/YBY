from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "YBY Hub"
    environment: str = "development"
    ollama_base_url: str = "http://localhost:11434"
    qdrant_url: str = "http://localhost:6333"
    default_model: str = "qwen2.5:3b-instruct-q4_K_M"
    approval_required: bool = True
    allowed_write_paths: str = "./workspace"
    log_level: str = "INFO"


settings = Settings()
