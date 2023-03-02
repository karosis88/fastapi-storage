from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Form
from fastapi import UploadFile

from src.auth.dependencies import get_self_id

from .schemas import FileView
from .schemas import StorageView
from .service import add_file_to_storage
from .service import get_files
from .service import get_or_create_storage
from .service import remove_file_by_name

router = APIRouter()


@router.post("/upload", response_model=FileView)
async def upload(self_user_id: int = Depends(get_self_id), file: UploadFile = Form()):
    return await add_file_to_storage(user_id=self_user_id, file=file)


@router.get("/info", response_model=StorageView)
async def see_storage(self_user_id: int = Depends(get_self_id)):
    return get_or_create_storage(self_user_id)


@router.get("/files", response_model=List[FileView])
async def files(self_user_id: int = Depends(get_self_id)):
    return get_files(self_user_id)


@router.post("/remove", response_model=FileView)
async def remove(
    file_name: str,
    self_user_id: int = Depends(get_self_id),
):
    return remove_file_by_name(user_id=self_user_id, file_name=file_name)
