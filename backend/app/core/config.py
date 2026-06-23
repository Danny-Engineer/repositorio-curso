from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Logística IA Lab Suite"
    DATABASE_URL: str = "postgresql+psycopg://lab:lab@localhost:5432/logistica_ia_lab"

    AI_PROVIDER: str = "local"

    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL: str = "gpt-4o-mini"

    ANTHROPIC_API_KEY: str | None = None
    ANTHROPIC_MODEL: str = "claude-3-5-sonnet-latest"

    class Config:
        env_file = ".env"

settings = Settings()
