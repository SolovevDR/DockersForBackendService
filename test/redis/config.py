from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str = Field(..., env="HOST")
    port: int = Field(..., env="PORT")

    redis_user: str = Field(..., env="REDIS_USER")
    redis_user_password: str = Field(..., env="REDIS_USER_PASSWORD")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


Settings = Settings()
print(Settings)