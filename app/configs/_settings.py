"""
Author: Ritvik Dayal
Description: Settings module for the backend application.
    This module is responsible for loading and validating the application settings.
"""
import os
from enum import Enum
import logging

from pydantic_settings import BaseSettings

class EnvironmentEnum(str, Enum):
    """
    Enum class for the environment types.
    """
    TEST = "TEST"
    DEV = "DEV"
    STAGE = "STAGE"
    PROD = "PROD"

class Settings(BaseSettings):
    """
    Settings class for the application.
    """
    APP_NAME: str = "ccs-aggregator"
    ENV: EnvironmentEnum = (
        EnvironmentEnum(os.environ["API_ENV"])
        if "API_ENV" in os.environ
        else EnvironmentEnum.TEST
    )

    logging.basicConfig(
        level = logging.INFO if ENV == EnvironmentEnum.PROD else logging.DEBUG,
        format = "%(asctime)s - %(name)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
    )

    SECRET_KEY: str = os.environ.get("SECRET_KEY", "test_secret_key@localhost12345678")
    DEBUG: bool = False

    Logger: logging.Logger = logging.getLogger(APP_NAME)

settings = Settings()
