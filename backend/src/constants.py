from pydantic import BaseSettings
from pydantic import Field


class Environment(BaseSettings):
    DB_URL: str = Field(min_length=1)

    class Config:
        env_file = "src/.env"


env = Environment()
DB_URL = env.DB_URL
