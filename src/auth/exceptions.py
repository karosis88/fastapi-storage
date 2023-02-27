from fastapi import HTTPException


class UserNotFound(HTTPException):
    ...


class UserCreationFailed(HTTPException):
    ...


class InvalidFriendRequest(HTTPException):
    ...


class FriendshipNotFound(HTTPException):
    ...
