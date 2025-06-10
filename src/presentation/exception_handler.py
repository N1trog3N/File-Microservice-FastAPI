from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from src.application.exceptions.core_exception import CoreException


async def exception_handler(
    request: Request, exc: CoreException
) -> Response:
    return JSONResponse(
        status_code=exc.status_code, content={"error": exc.message, **exc.detail}
    )
