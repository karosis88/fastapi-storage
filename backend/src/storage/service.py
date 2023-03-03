from typing import List

from fastapi import HTTPException
from fastapi import UploadFile
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.database import SessionLocal
from src.storage.models import Storage

from .models import File


def get_or_create_storage(user_id: int) -> Storage:
    with SessionLocal(expire_on_commit=False) as session:
        stmt = (
            select(Storage)
            .where(Storage.owner_id == user_id)
            .options(joinedload(Storage.files))
        )
        storage = session.scalar(stmt)
        total_size = 0
        if not storage:
            storage = Storage(owner_id=user_id)
            session.add(storage)
            session.commit()
        else:
            for file in storage.files:
                total_size += file.size

        storage.used_space_kb = total_size
        return storage


async def add_file_to_storage(user_id: int, file: UploadFile) -> File:
    with SessionLocal(expire_on_commit=False) as session:
        stmt = (
            select(Storage)
            .where(Storage.owner_id == user_id)
            .options(joinedload(Storage.files))
        )
        storage = session.scalar(stmt)
        if not storage:
            raise HTTPException(status_code=404, detail="Storage was not found")

        fsize = int(file.size)
        storage_used_kb = sum(file.size for file in storage.files)
        available_space = storage.maxium_space_kb - storage_used_kb
        if fsize > available_space:
            raise HTTPException(status_code=403, detail="Not enough space")

        fname = file.filename
        new_file = File(
            storage_id=storage.id, binary_data=await file.read(), size=fsize, name=fname
        )
        storage.files.append(new_file)
        session.commit()
        return new_file


def get_files(user_id: int) -> List[File]:
    with SessionLocal(expire_on_commit=False) as session:
        stmt = (
            select(Storage)
            .options(joinedload(Storage.files))
            .where(Storage.owner_id == user_id)
        )
        storage = session.scalar(stmt)
        if not storage:
            raise HTTPException(status_code=404, detail="Storage was not found")
        return storage.files


def remove_file_by_name(user_id: int, file_name: str) -> File:
    with SessionLocal(expire_on_commit=False) as session:
        stmt = (
            select(Storage)
            .where(Storage.owner_id == user_id)
            .options(joinedload(Storage.files))
        )
        storage = session.scalar(stmt)
        if not storage:
            raise HTTPException(status_code=404, detail="Storage was not found")

        for file in storage.files:
            if file.name == file_name:
                session.delete(file)
                session.commit()
                break
        else:
            raise HTTPException(status_code=404, detail="File not found")
        return file


def download_file_by_name(user_id: int, file_name: str):
    with SessionLocal(expire_on_commit=False) as session:
        stmt = (
            select(Storage)
            .where(Storage.owner_id == user_id)
            .options(joinedload(Storage.files))
        )
        storage = session.scalar(stmt)
        if not storage:
            raise HTTPException(status_code=404, detail="Storage was not found")
        for file in storage.files:
            if file.name == file_name:
                break
        else:
            raise HTTPException(status_code=404, detail="File not found")
        return file.binary_data