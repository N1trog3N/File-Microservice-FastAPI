from abc import ABC, abstractmethod

from src.application.irepos.i_file_repo import IFileRepo


class AbstractUnitOfWork(ABC):

    image_repo: IFileRepo

    async def __aenter__(self) -> "AbstractUnitOfWork":
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, *args, **kwargs
    ) -> None:
        if not exc_type:
            await self.commit()

        await self.close()

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass

    @abstractmethod
    async def close(self):
        pass
