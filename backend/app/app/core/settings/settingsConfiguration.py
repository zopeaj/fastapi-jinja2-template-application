from pydantic import BaseSettings

class Settings(BaseSettings):
    appName: str = "App Name"
    openapi_url: str = ''


settings = Settings()
