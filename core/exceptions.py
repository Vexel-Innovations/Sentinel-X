from fastapi import Request, status
from fastapi.responses import JSONResponse
from sentinel_x.core.logging import logger

async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception caught: {str(exc)}", extra={"path": request.url.path})
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "An internal error occurred in SENTINEL-X. Our team has been notified.", "detail": str(exc)},
    )
