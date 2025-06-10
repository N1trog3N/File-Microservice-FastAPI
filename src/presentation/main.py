from contextlib import asynccontextmanager

import fastapi

from src.core.containers import Container
from src.application.exceptions.core_exception import CoreException
from src.presentation.api.router import router
from src.presentation.exception_handler import exception_handler


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    container = Container()
    storage_client = container.storage.client()
    await storage_client.ensure_bucket_exists()
    yield


def create_app() -> fastapi.FastAPI:
    app = fastapi.FastAPI(
        lifespan=lifespan,
        title="File Microservice",
        version="0.9.1",
    )
    container = Container()
    container.wire(packages=["src.presentation.api"])
    app.container = container

    app.include_router(router)
    app.add_exception_handler(CoreException, exception_handler)

    return app


app = create_app()
