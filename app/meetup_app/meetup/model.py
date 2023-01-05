import os

from sqlalchemy import Integer, Column, String, TIMESTAMP, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
url_object = URL.create(
    "postgresql",
    username=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD"),
    host=os.environ.get("POSTGRES_HOST"),
    port=os.environ.get("POSTGRES_PORT"),
    database=os.environ.get("POSTGRES_DBNAME"),
    )
engine = create_engine(url_object)
Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=engine)


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True)
    password_hash = Column(String)


class MeetupModel(Base):
    __tablename__ = "meetup"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    keywords = Column(ARRAY(String))
    place = Column(String)
    date = Column(TIMESTAMP())
    created_by = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"),
                        nullable=False)
