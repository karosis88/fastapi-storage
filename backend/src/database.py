from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from .constants import DB_URL

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
BASE = declarative_base()
