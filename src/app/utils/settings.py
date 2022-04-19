from pydantic import BaseSettings

__all__ = 'settings',

class Settings(BaseSettings):
    LOCAL: str
    DEBUG: bool = False

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()