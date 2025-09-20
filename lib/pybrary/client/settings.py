from functools import cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_url = "http://localhost:9001"


@cache
def get_settings() -> Settings:
    return Settings()
