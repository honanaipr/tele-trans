from .schemas import User
from .exceptions import StorageError
from . import models, schemas
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///db.sqlite3", echo=True)


def get_db() -> Session:
    return Session(engine)


def add_user(db: Session, user: schemas.User):
    db_user = models.User(**user.model_dump(by_alias=True))
    db.add(db_user)
    db.commit()


def get_user_by_id(db: Session, id: int) -> schemas.User:
    return schemas.User.model_validate(db.query(models.User).where(models.User.id == id).first())


def if_user_exist(db: Session, user: schemas.User) -> bool:
    return db.query(exists().where(models.User.id == user.id)).scalar()
