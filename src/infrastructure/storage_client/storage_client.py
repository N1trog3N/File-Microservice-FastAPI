import aioboto3
from botocore.exceptions import ClientError
from typing import BinaryIO

from src.core.config import settings
from src.application.common.i_storage_client import IStorageClient
from src.application.exceptions.file_exceptions import FileNotFoundException


class S3StorageClient(IStorageClient):
    def __init__(self):
        self.endpoint_url = settings.MINIO_ENDPOINT_URL
        self.access_key = settings.MINIO_ACCESS_KEY
        self.secret_key = settings.MINIO_SECRET_KEY
        self.bucket_name = settings.MINIO_BUCKET_NAME
        self.session = aioboto3.Session()

    async def _get_client(self):
        return self.session.client(
            "s3",
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
        )

    async def ensure_bucket_exists(self) -> None:
        async with await self._get_client() as client:
            existing = await client.list_buckets()
            if not any(b["Name"] == self.bucket_name for b in existing["Buckets"]):
                await client.create_bucket(Bucket=self.bucket_name)

    async def upload_file(
        self, file_obj: BinaryIO, s3_key: str, content_type: str = "image/jpeg"
    ) -> str:
        async with await self._get_client() as client:
            await client.upload_fileobj(
                Fileobj=file_obj,
                Bucket=self.bucket_name,
                Key=s3_key,
                ExtraArgs={"ContentType": content_type},
            )
            return await self.get_file_url(s3_key)

    async def get_file_url(self, s3_key: str, expires_in: int = 3600) -> str:
        async with await self._get_client() as client:
            try:
                return await client.generate_presigned_url(
                    ClientMethod="get_object",
                    Params={"Bucket": self.bucket_name, "Key": s3_key},
                    ExpiresIn=expires_in,
                )
            except ClientError:
                raise FileNotFoundException

    async def delete_file(self, s3_key: str) -> None:
        async with await self._get_client() as client:
            await client.delete_object(Bucket=self.bucket_name, Key=s3_key)
