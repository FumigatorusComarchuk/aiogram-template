from os import environ as env

from pydantic import Field, BaseModel


class TelegramConfig(BaseModel):
    bot_token: str = Field(alias="TELEGRAM_BOT_TOKEN")


class PostgresConfig(BaseModel):
    host: str = Field(alias="POSTGRES_HOST")
    port: int = Field(alias="POSTGRES_PORT")
    login: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")
    database: str = Field(alias="POSTGRES_DB")


class Config(BaseModel):
    telegram: TelegramConfig = Field(
        default_factory=lambda: TelegramConfig(**env))
    postgres: PostgresConfig = Field(
        default_factory=lambda: PostgresConfig(**env))
