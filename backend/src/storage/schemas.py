from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class StorageView(BaseModel):
    id: int
    owner_id: int
    maxium_space_kb: int
    used_space_kb: int
    created_at: datetime

    class Config:
        orm_mode = True


class FileView(BaseModel):
    id: int
    storage_id: int
    size: int
    name: str
    uploaded_at: datetime
    last_downloaded_at: Optional[datetime]

    class Config:
        orm_mode = True
