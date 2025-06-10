import jwt
from fastapi import Depends
from fastapi.security import HTTPBearer

from src.core.config import settings
from src.application.exceptions.authentication_exceptions import (
    UserUnauthorizedException,
    TokenExpiredException,
    InvalidTokenException,
    InvalidTokenTypeException,
)

auth_scheme = HTTPBearer()


async def get_current_user(token=Depends(auth_scheme)):
    if not token or token.scheme != "Bearer":
        raise UserUnauthorizedException
    secret_key = settings.JWT_SECRET_KEY
    algorithm = settings.ALGORITHM
    try:
        payload = jwt.decode(token.credentials, key=secret_key, algorithms=[algorithm])
    except jwt.ExpiredSignatureError:
        raise TokenExpiredException
    except jwt.DecodeError:
        raise InvalidTokenException
    if payload["type"] != "access":
        raise InvalidTokenTypeException
