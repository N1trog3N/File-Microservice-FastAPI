from dependency_injector import containers, providers

from src.application.use_cases.get_file_url import GetFileURLUseCase
from src.application.use_cases.upload_file import UploadFileUseCase
from src.application.use_cases.update_file import UpdateFileUseCase
from src.application.use_cases.remove_file import RemoveFileUseCase
from src.infrastructure.storage_client.storage_client import S3StorageClient


class StorageContainer(containers.DeclarativeContainer):
    client = providers.Singleton(S3StorageClient)


class Container(containers.DeclarativeContainer):

    storage = providers.Container(StorageContainer)

    get_url_use_case = providers.Factory(
        GetFileURLUseCase,
        storage_client=storage.client,
    )
    upload_file_use_case = providers.Factory(
        UploadFileUseCase,
        storage_client=storage.client,
    )
    update_file_use_case = providers.Factory(
        UpdateFileUseCase,
        storage_client=storage.client,
    )
    remove_file_use_case = providers.Factory(
        RemoveFileUseCase,
        storage_client=storage.client,
    )
