from .schemas import User
from .exceptions import StorageError, UserExistError, UserNotExistError
from . import models, schemas
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import Session
from collections.abc import Callable
from functools import wraps
from typing import TypeVar, ParamSpec
from sqlalchemy.exc import IntegrityError

engine = create_engine("sqlite:///db.sqlite3", echo=True)

T = TypeVar("T")
P = ParamSpec("P")


def db_operation(f: Callable[P, T]) -> Callable[P, T]:
    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as exp:
            if isinstance(exp, StorageError):
                raise
            else:
                raise StorageError from exp

    return wrapper


@db_operation
def get_db() -> Session:
    return Session(engine)


@db_operation
def add_user(db: Session, user: schemas.User):
    try:
        db_user = models.User(**user.model_dump(by_alias=True))
        db.add(db_user)
        db.commit()
    except IntegrityError as exp:
        if (
            exp.args
            and len(exp.args)
            and "UNIQUE constraint failed" in exp.args[0]
            and "users.id" in exp.args[0]
        ):
            raise UserExistError
        raise


@db_operation
def get_user_by_id(db: Session, id: int) -> schemas.User:
    return schemas.User.model_validate(
        db.query(models.User).where(models.User.id == id).first()
    )


@db_operation
def if_user_exist(db: Session, user: schemas.User) -> bool:
    return db.query(exists(models.User).where(models.User.id == user.id)).scalar()


@db_operation
def delete_user(db: Session, user: schemas.User):
    num_deleted = db.query(models.User).where(models.User.id == user.id).delete()
    db.commit()
    if not num_deleted:
        raise UserNotExistError
