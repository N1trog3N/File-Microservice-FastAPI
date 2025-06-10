from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class FileEntity:
    id: UUID
    type: str
    key: str
    updated_at: datetime
    created_at: datetime
    