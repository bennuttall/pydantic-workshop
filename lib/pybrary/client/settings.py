from functools import cache

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="pyb_", extra="ignore")

    api_url: AnyHttpUrl


@cache
def get_settings() -> Settings:
    return Settings()
