from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from .dependencies import get_self
from .dependencies import get_self_id
from .dependencies import get_user_id
from .dependencies import is_admin
from .models import User
from .schemas import FriendsView
from .schemas import UserAdminView
from .schemas import UserCreate
from .schemas import UserView
from .service import approve_friend_request
from .service import authenticate
from .service import create_jwt
from .service import create_user
from .service import get_all_users
from .service import get_friends
from .service import get_received_requests
from .service import get_sent_requests
from .service import get_user_by_username
from .service import remove_user
from .service import send_friend_request

router = APIRouter()


@router.post("/signup", response_model=UserView)
def create(user: UserCreate):
    return create_user(user)


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username, password = form_data.username, form_data.password
    user = get_user_by_username(username)
    if not authenticate(hashed_password=user.password, raw_password=password):
        raise HTTPException(status_code=403, detail="Invalid username or password")
    payload = {
        "id": user.id,
        "username": user.username,
    }

    return {"access_token": create_jwt(payload)}


@router.post("/remove", response_model=UserView)
def remove(self_user_id: int = Depends(get_self_id)):
    return remove_user(self_user_id)


@router.get("/me", response_model=UserView)
def me(self_user: User = Depends(get_self)):
    return self_user


@router.post("/add_friend")
def add_friend(self_user_id=Depends(get_self_id), user_id=Depends(get_user_id)):
    if user_id == self_user_id:
        raise HTTPException(status_code=400, detail="Can't add yourself to friends")
    send_friend_request(initiator_user=self_user_id, user=user_id)
    return "successful added"


@router.get("/friends", response_model=List[UserView])
def friends(self_user_id=Depends(get_self_id)):
    return get_friends(self_user_id)


@router.get("/approve_friend", response_model=FriendsView)
def approve_friend(
    self_user_id=Depends(get_self_id), user_id: int = Depends(get_user_id)
):
    return approve_friend_request(approver=self_user_id, user_id=user_id)


@router.get("/sent_friend_requests", response_model=List[UserView])
def friend_sent_requests(self_user_id=Depends(get_self_id)):
    res = get_sent_requests(self_user_id)
    return res


@router.get("/received_friend_requests", response_model=List[UserView])
def friend_received_requests(self_user_id=Depends(get_self_id)):
    return get_received_requests(self_user_id)


@router.get(
    "/all_users", response_model=List[UserAdminView], dependencies=[Depends(is_admin)]
)
def all_users():
    return get_all_users()
