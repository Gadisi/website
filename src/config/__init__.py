from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_URL: str = "tdkgadisifoundation.com"
    SECRET_KEY = "aaaa"


def config_instance() -> Settings:
    return Settings()
