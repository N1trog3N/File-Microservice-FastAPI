from src.application.common.i_storage_client import IStorageClient


class GetFileURLUseCase:
    def __init__(self, storage_client: IStorageClient):
        self.storage_client = storage_client

    async def execute(self, s3_key: str) -> str:
        return await self.storage_client.get_file_url(s3_key)
