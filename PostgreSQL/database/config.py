from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_db: str = Field(..., env="POSTGRES_DB")
    postgres_user: str = Field(..., env="POSTGRES_USER")
    postgres_password: str = Field(..., env="POSTGRES_PASSWORD")

    db_host: str = Field(..., env="DB_HOST")
    db_port: str = Field(..., env="DB_PORT")
    db_port_local: str = Field(..., env="DB_PORT_LOCAL")
    db_name: str = Field(..., env="DB_NAME")
    db_user: str = Field(..., env="DB_USER")
    db_pass: str = Field(..., env="DB_PASS")

    first_user_login: str = Field(..., env="FIRST_USER_LOGIN")
    first_user_password: str = Field(..., env="FIRST_USER_PASSWORD")
    first_user_role: str = Field(..., env="FIRST_USER_ROLE")

    second_user_login: str = Field(..., env="SECOND_USER_LOGIN")
    second_user_password: str = Field(..., env="SECOND_USER_PASSWORD")
    second_user_role: str = Field(..., env="SECOND_USER_ROLE")

    first_role: str = Field(..., env="FIRST_ROLE")
    second_role: str = Field(..., env="SECOND_ROLE")

    is_init_data_alembic: str = Field(..., env="IS_INIT_DATA_ALEMBIC")
    is_init_data_python: str = Field(..., env="IS_INIT_DATA_PYTHON")

    class Config:
        env_file = "../.db.env"
        env_file_encoding = "utf-8"


Settings = Settings()
