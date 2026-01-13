from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
import logging

def add_exception_handlers(app: FastAPI):
    """
    Add exception handlers to return safe error messages to users
    """
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """
        Handle general exceptions and return safe error messages
        """
        # Log the actual error for debugging (only visible to developers)
        logging.error(f"Unexpected error occurred: {exc}", exc_info=True)
        
        # Return a safe error message to the user
        return JSONResponse(
            status_code=500,
            content={
                "error": "An unexpected error occurred",
                "message": "Please try again later or contact support if the problem persists."
            }
        )
    
    @app.exception_handler(SQLAlchemyError)
    async def database_exception_handler(request: Request, exc: SQLAlchemyError):
        """
        Handle database-related exceptions and return safe error messages
        """
        # Log the actual error for debugging
        logging.error(f"Database error occurred: {exc}", exc_info=True)
        
        # Return a safe error message to the user
        return JSONResponse(
            status_code=500,
            content={
                "error": "A database error occurred",
                "message": "We're experiencing issues with our database. Please try again later."
            }
        )

# Example usage in main app
# add_exception_handlers(app)