from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID

from src.domain.entities.file import FileEntity


class IFileRepo(ABC):

    @abstractmethod
    async def get_file(self, file_id: UUID) -> FileEntity:
        pass

    @abstractmethod
    async def upload_file(
        self, file_id: UUID, file_type: str, key: str, updated_at: datetime, created_at: datetime
    ) -> FileEntity:
        pass

    @abstractmethod
    async def update_file(
            self, file_id: UUID, file_type: str, key: str, updated_at: datetime, created_at: datetime
    ) -> FileEntity:
        pass

    @abstractmethod
    async def delete_file(self, file_id: UUID) -> None:
        pass
    