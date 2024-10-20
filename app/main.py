"""
Author: Ritvik Dayal
Description: Entry point for the backend application.
    This module is responsible for creating the FastAPI application and running the server.
"""

import uvicorn
from fastapi import FastAPI
from app.configs._settings import settings

app: FastAPI = FastAPI(
    title=settings.APP_NAME,
    version="0.1",
    docs_url=f"/api/{settings.APP_NAME}/docs",
    redoc_url=f"/api/{settings.APP_NAME}/redoc",
    openapi_url=f"/api/{settings.APP_NAME}/openapi.json",
    description=f"API Contract for {settings.APP_NAME} API",
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
