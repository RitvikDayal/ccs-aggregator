"""
Health Check Router: This router is used to check the health of the application.
"""

from fastapi import APIRouter
from app.configs.general_config import ServiceResponse

router = APIRouter(
    tags=["Health Check"],
    prefix="/v1/health-check",
)

@router.get("/")
def health_check():
    """
    Health Check Endpoint:
    This endpoint is used to check the health of the application.
    """
    return ServiceResponse.success("Application is running.")
