from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship
from src.database import BASE

from .schemas import FriendsState


class Friends(BASE):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True)
    initiator_user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    state = Column(Enum(FriendsState))
    created_at = Column(DateTime, default=datetime.now())

    initiator_user = relationship("User", foreign_keys=[initiator_user_id])
    user = relationship("User", foreign_keys=[user_id])

    __table_args__ = (UniqueConstraint(initiator_user_id, user_id, name="unfriend"),)

    def __repr__(self):
        return f"Friends<{self.initiator_user} with {self.user}>"


class User(BASE):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    email = Column(String, nullable=True)
    admin = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"User<{self.username}>"
