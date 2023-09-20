from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String, default="")
    user_name = Column(String, default="")


engine = create_engine("sqlite:///db.sqlite3", echo=True)
Base.metadata.create_all(engine)
