from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from .models import User
from .service import decode_jwt
from .service import get_user_by_id
from .service import get_user_by_username

oauth = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_self_id(token: str = Depends(oauth)):
    payload = decode_jwt(token)
    return payload["id"]


def get_self(user_id=Depends(get_self_id)):
    return get_user_by_id(user_id=user_id)


def get_user(user: str):
    return get_user_by_username(user)


def get_user_id(user: str):
    return get_user_by_username(user).id


def is_admin(user: User = Depends(get_self)):
    if not user.admin:
        raise HTTPException(status_code=403, detail="Access denied")
