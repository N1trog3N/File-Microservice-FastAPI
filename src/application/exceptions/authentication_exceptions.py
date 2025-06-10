from src.application.exceptions.core_exception import CoreException


class UserUnauthorizedException(CoreException):
    def __init__(self):
        super().__init__(
            status_code=401,
            message="Unauthorized user.",
        )


class TokenExpiredException(CoreException):
    def __init__(self):
        super().__init__(
            status_code=401,
            message="Provided token expired.",
        )


class InvalidTokenException(CoreException):
    def __init__(self):
        super().__init__(
            status_code=401,
            message="Invalid token provided.",
        )


class InvalidTokenTypeException(CoreException):
    def __init__(self):
        super().__init__(
            status_code=401,
            message="Invalid token type provided.",
        )
