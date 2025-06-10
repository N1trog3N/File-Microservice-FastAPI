from abc import ABC, abstractmethod
from typing import BinaryIO


class IStorageClient(ABC):
    @abstractmethod
    async def upload_file(
        self, file_obj: BinaryIO, s3_key: str, content_type: str = "image/jpeg"
    ) -> str:
        """Загружает файл и возвращает публичную ссылку"""
        pass

    @abstractmethod
    async def get_file_url(self, s3_key: str, expires_in: int = 3600) -> str:
        """Возвращает временную ссылку на файл"""
        pass

    @abstractmethod
    async def delete_file(self, s3_key: str) -> None:
        """Удаляет файл из хранилища"""
        pass

    @abstractmethod
    async def ensure_bucket_exists(self) -> None:
        """Создаёт бакет, если он не существует"""
        pass
