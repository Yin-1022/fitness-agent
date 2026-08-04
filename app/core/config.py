from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Fitness Agent API"
    database_url: str = "sqlite:///./fitness_agent.db"

    class Config:
        env_file = ".env"

settings = Settings()