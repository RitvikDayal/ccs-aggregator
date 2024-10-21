"""
Author: Ritvik Dayal
Description: Entry point for the backend application.
    This module is responsible for creating the FastAPI application and running the server.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.configs._settings import settings
from app.routers import health_check_router

app: FastAPI = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    description="API Contract for {settings.APP_NAME} API",
    root_path="/{settings.PREFIX}",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(
    health_check_router,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
