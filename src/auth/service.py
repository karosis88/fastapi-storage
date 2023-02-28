from hashlib import md5
from typing import List

import sqlalchemy.exc
from jose import jwt
from sqlalchemy import delete
from sqlalchemy import select

from src.auth.models import User
from src.database import SessionLocal

from .constants import JWT_SECRET_KEY
from .exceptions import InvalidApproveRequest
from .exceptions import InvalidFriendRequest
from .exceptions import UserCreationFailed
from .exceptions import UserNotFound
from .models import Friends
from .models import FriendsState
from .schemas import UserCreate


def authenticate(hashed_password, raw_password):
    return hashed_password == hash_password(raw_password)


def hash_password(password):
    return md5(password.encode()).hexdigest()


def create_jwt(payload):
    return jwt.encode(payload, JWT_SECRET_KEY)


def decode_jwt(payload):
    return jwt.decode(payload, JWT_SECRET_KEY)


def create_user(user: UserCreate) -> User:
    with SessionLocal(expire_on_commit=False) as session:
        try:
            username = user.username
            password = user.password
            user = User(username=username, password=hash_password(password))
            session.add(user)
            session.commit()
            return user
        except Exception:
            # TODO: log e
            raise UserCreationFailed(status_code=400, detail="User can not be created.")


def remove_user(user_id: int) -> User:
    with SessionLocal(expire_on_commit=False) as session:
        stmt = delete(User).where(User.id == user_id).returning(User)
        user = session.scalar(stmt)
        session.commit()
        return user


def get_user_by_username(username: str) -> User:
    with SessionLocal() as session:
        stmt = select(User).where(User.username == username)
        user = session.scalar(stmt)
        if not user:
            raise UserNotFound(status_code=404, detail="User not found.")
        return user


def get_user_by_id(user_id: int) -> User:
    with SessionLocal() as session:
        stmt = select(User).where(User.id == user_id)
        user = session.scalar(stmt)
        if not user:
            raise UserNotFound(status_code=404, detail="User not found.")
        return user


def send_friend_request(initiator_user: int, user: int):
    with SessionLocal() as session:
        stmt = (
            select(Friends)
            .where(Friends.initiator_user_id == user)
            .where(Friends.user_id == initiator_user)
        )
        if session.scalar(stmt):
            raise InvalidFriendRequest(
                status_code=400, detail="You have already been requested by this user."
            )
        friendship = Friends(
            initiator_user_id=initiator_user, user_id=user, state=FriendsState.Requested
        )
        session.add(friendship)
        try:
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            raise InvalidFriendRequest(
                status_code=400,
                detail="You have already sent this user a friend request.",
            )


def get_friends(user_id: int) -> List[User]:
    with SessionLocal() as session:
        stmt = (
            select(User)
            .join(Friends.user)
            .where(Friends.initiator_user_id == user_id)
            .where(Friends.state == FriendsState.Approved)
        )
        initiated_users = session.scalars(stmt).all()
        stmt = (
            select(User)
            .join(Friends.initiator_user)
            .where(Friends.user_id == user_id)
            .where(Friends.state == FriendsState.Approved)
        )
        initiated_by = session.scalars(stmt).all()

        if not initiated_users and not initiated_by:
            return []
        return initiated_users + initiated_by


def get_sent_requests(user_id: int) -> List[User]:
    with SessionLocal() as session:
        stmt = (
            select(User)
            .join(Friends.user)
            .where(Friends.initiator_user_id == user_id)
            .where(Friends.state == FriendsState.Requested)
        )
        return session.scalars(stmt).all()


def get_received_requests(user_id: int) -> List[User]:
    with SessionLocal() as session:
        stmt = (
            select(User)
            .join(Friends.initiator_user)
            .where(Friends.user_id == user_id)
            .where(Friends.state == FriendsState.Requested)
        )
        return session.scalars(stmt).all()


def approve_friend_request(approver: int, user_id: int):
    with SessionLocal(expire_on_commit=False) as session:
        stmt = (
            select(Friends)
            .where(Friends.initiator_user_id == user_id)
            .where(Friends.user_id == approver)
        )
        friendship = session.scalar(stmt)
        if not friendship:
            raise InvalidApproveRequest(
                status_code=400, detail="This user did not send you a friend request."
            )
        if friendship.state == FriendsState.Approved:
            raise InvalidApproveRequest(
                status_code=400, detail="You are already friends with this user."
            )
        friendship.state = FriendsState.Approved
        session.commit()
        return friendship


def get_all_users():
    with SessionLocal(expire_on_commit=False) as session:
        stmt = select(User)
        return session.scalars(stmt).all()
