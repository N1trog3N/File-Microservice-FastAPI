from src.application.common.i_storage_client import IStorageClient


class RemoveFileUseCase:
    def __init__(self, storage_client: IStorageClient):
        self.storage_client = storage_client

    async def execute(self, s3_key: str) -> None:
        await self.storage_client.delete_file(s3_key)
