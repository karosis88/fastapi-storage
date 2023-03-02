import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import LargeBinary
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship

from src.auth.models import User
from src.database import BASE


class Storage(BASE):
    __tablename__ = "storage"

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey("users.id"))
    owner = relationship(User, uselist=False, backref="storage")
    maxium_space_kb = Column(Integer, default=50_000_000)

    files = relationship("File", back_populates="storage")
    created_at = Column(DateTime, default=datetime.datetime.now())

    __table_args__ = (UniqueConstraint(owner_id, name="unstorage"),)


class File(BASE):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    storage_id = Column(ForeignKey("storage.id"))
    size = Column(Integer)
    binary_data = Column(LargeBinary)

    uploaded_at = Column(DateTime, default=datetime.datetime.now())
    last_downloaded_at = Column(DateTime, default=None)

    storage = relationship(Storage, back_populates="files")

    __table_args__ = (UniqueConstraint(name, name="unname"),)
