from typing import Any

from pydantic import BaseModel, validator


class S3StorageConnectionInfo(BaseModel):
    access_id: str
    access_key: str
    bucket_name: str

    @validator("access_id", "access_key", "bucket_name")
    def not_empty(cls, value) -> Any:
        if not value:
            raise ValueError("Field cannot be empty")
        return value
