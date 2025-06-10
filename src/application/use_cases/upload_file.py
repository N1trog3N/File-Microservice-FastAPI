from typing import BinaryIO

from src.application.common.i_storage_client import IStorageClient


class UploadFileUseCase:
    def __init__(self, storage_client: IStorageClient):
        self.storage_client = storage_client

    async def execute(
        self, file_obj: BinaryIO, s3_key: str, content_type: str = "image/jpeg"
    ) -> str:
        return await self.storage_client.upload_file(file_obj, s3_key, content_type)
