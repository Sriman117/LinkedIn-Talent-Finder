from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    postgres_url: str
    qdrant_host: str = "http://localhost:6333"
    embedding_dim: int = 384

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
