from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class FriendsState(Enum):
    Requested = "Requested"
    Blocked = "Blocked"
    Approved = "Approved"


class UserCreate(BaseModel):
    username: str
    password: str


class UserView(BaseModel):
    id: int
    username: str
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]

    class Config:
        orm_mode = True


class FriendsView(BaseModel):
    initiator_user: int
    user: int
    state: FriendsState

    class Config:
        orm_mode = True
