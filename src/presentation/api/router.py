from fastapi import APIRouter

from src.presentation.api.endpoints.files import router as file_router

router = APIRouter(prefix="")
router.include_router(file_router)
