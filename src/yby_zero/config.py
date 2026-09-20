from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    yby_env: str = "development"
    yby_log_level: str = "INFO"
    yby_default_privacy: str = "P1"
    yby_default_latency_ms: int = 2000
    yby_cloud_enabled: bool = False
    ollama_base_url: str = "http://127.0.0.1:11434"
    ollama_model: str = ""
    openrouter_api_key: str = ""
    openrouter_model: str = ""
    gemini_api_key: str = ""
    openai_api_key: str = ""


settings = Settings()
