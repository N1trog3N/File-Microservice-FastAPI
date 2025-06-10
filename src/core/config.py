from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MINIO_ENDPOINT_URL: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_BUCKET_NAME: str
    MINIO_REGION: str
    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str
    JWT_SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()
