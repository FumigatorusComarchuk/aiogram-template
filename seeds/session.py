from os import environ as env

from pydantic import Field, BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine


class PostgresConfig(BaseModel):
    host: str = Field(alias="POSTGRES_HOST")
    port: int = Field(alias="POSTGRES_PORT")
    login: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")
    database: str = Field(alias="POSTGRES_DB")


psql_config = PostgresConfig(**env)


def new_session_maker() -> async_sessionmaker[AsyncSession]:
    psql_config = PostgresConfig(**env)
    database_uri = (
        "postgresql+psycopg://{login}:{password}@{host}:{port}/{database}".format(
            login=psql_config.login,
            password=psql_config.password,
            host=psql_config.host,
            port=psql_config.port,
            database=psql_config.database,
        )
    )

    engine = create_async_engine(
        database_uri,
        pool_size=15,
        max_overflow=15,
        connect_args={
            "connect_timeout": 5,
        },
    )
    return async_sessionmaker(
        engine, class_=AsyncSession, autoflush=False, expire_on_commit=False
    )
