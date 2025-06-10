from fastapi import APIRouter, UploadFile, Depends, File, Query
from dependency_injector.wiring import inject, Provide

from src.core.containers import Container
from src.presentation.api.authentication_dependencies import get_current_user
from src.application.use_cases.upload_file import UploadFileUseCase
from src.application.use_cases.get_file_url import GetFileURLUseCase
from src.application.use_cases.remove_file import RemoveFileUseCase
from src.application.use_cases.update_file import UpdateFileUseCase

router = APIRouter(prefix="/files", tags=["files"])


@router.post("/upload")
@inject
async def upload_file(
    file: UploadFile = File(...),
    s3_key: str = Query(...),
    user=Depends(get_current_user),
    upload_file_use_case: UploadFileUseCase = Depends(Provide[Container.upload_file_use_case]),
):
    url = await upload_file_use_case.execute(file_obj=file.file, s3_key=s3_key, content_type=file.content_type)
    return {"url": url}


@router.get("/url")
@inject
async def get_file_url(
    s3_key: str = Query(..., description="Ключ файла в S3 для получения ссылки"),
    user=Depends(get_current_user),
    get_file_url_use_case: GetFileURLUseCase = Depends(Provide[Container.get_url_use_case]),
):
    url = await get_file_url_use_case.execute(s3_key=s3_key)
    return {"url": url}


@router.delete("/")
@inject
async def delete_file(
    s3_key: str = Query(..., description="Ключ файла, который нужно удалить"),
    user=Depends(get_current_user),
    remove_file_use_case: RemoveFileUseCase = Depends(Provide[Container.remove_file_use_case]),
):
    await remove_file_use_case.execute(s3_key=s3_key)
    return {"status": "deleted"}


@router.put("/update")
@inject
async def update_file(
    file: UploadFile = File(..., description="Новый файл для замены"),
    s3_key: str = Query(..., description="Ключ заменяемого файла"),
    user=Depends(get_current_user),
    update_file_use_case: UpdateFileUseCase = Depends(Provide[Container.update_file_use_case]),
):
    url = await update_file_use_case.execute(file_obj=file.file, s3_key=s3_key, content_type=file.content_type)
    return {"url": url}
