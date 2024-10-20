
"""
Author: Ritvik Dayal
Description: This file contains the general configurations for the FastAPI application.
"""
from fastapi import status
from fastapi.responses import JSONResponse

class ServiceResponse:
    """
    Helper class to generate responses for FastAPI.
    At this point in time we expect all responses to have uniform headers
    """

    @classmethod
    def custom(cls, content, response_code) -> JSONResponse:
        """
        Method to generate a custom response for the FastAPI application.
        
        :param content: The content to be sent in the response.
        :param response_code: The HTTP response code to be sent.
        
        :return: A JSONResponse object with the specified content and response code.
        """
        if content not in ["dict", "list"]:
            content = {"message": content}

        return JSONResponse(
            content=content,
            status_code=response_code,
            headers={
                "content-type": "application/json",
                "access-control-allow-credentials": "true",
            },
        )

    @classmethod
    def success(cls, content):
        """
        Success response with status code 200.
        
        :param content: The content to be sent in the response.
        
        :return: A JSONResponse object with the specified content and status code 200.
        """
        return cls.custom(content, status.HTTP_200_OK)

    @classmethod
    def unauthorized(cls, content):
        """
        Unauthorized response with status code 401.
        
        :param content: The content to be sent in the response.
        
        :return: A JSONResponse object with the specified content and status code 401.
        """
        return cls.custom(content, status.HTTP_401_UNAUTHORIZED)

    @classmethod
    def unprocessable(cls, content):
        """
        Unprocessable entity response with status code 422.
        
        :param content: The content to be sent in the response.
        
        :return: A JSONResponse object with the specified content and status code 422.
        """
        return cls.custom(content, status.HTTP_422_UNPROCESSABLE_ENTITY)

    @classmethod
    def internal_error(cls, content):
        """
        Internal server error response with status code 500.
        
        :param content: The content to be sent in the response.
        
        :return: A JSONResponse object with the specified content and status code 500.
        """
        return cls.custom(content, status.HTTP_500_INTERNAL_SERVER_ERROR)
