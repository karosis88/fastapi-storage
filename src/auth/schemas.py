from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional
from typing import Union

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
    age: Union[str, None]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]

    class Config:
        orm_mode = True


class FriendsView(BaseModel):
    initiator_user_id: int
    user_id: int
    state: FriendsState

    class Config:
        orm_mode = True


class UserAdminView(UserView):
    admin: bool
    created_at: datetime
