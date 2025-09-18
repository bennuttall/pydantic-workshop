from functools import cache

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="pyb_", extra="ignore")

    books_dir: DirectoryPath


@cache
def get_settings() -> Settings:
    return Settings()
