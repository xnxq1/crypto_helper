import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=f"{pathlib.Path(__file__).resolve().parent.parent.parent}/.env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
    )

    TELEGRAM_KEY: str

