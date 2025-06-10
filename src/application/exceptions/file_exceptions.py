from src.application.exceptions.core_exception import CoreException


class FileNotFoundException(CoreException):
    def __init__(self):
        super().__init__(status_code=404, message="File not found.")