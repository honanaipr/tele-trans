from tele_trans.database import add_user, get_db, get_user_by_id, if_user_exist
from tele_trans.schemas import User
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tele_trans import models, schemas


@pytest.fixture
def session():
    engine = create_engine("sqlite://", echo=True)
    session = sessionmaker(engine)()
    models.Base.metadata.create_all(engine)
    yield session
    session.close()


def test_add_user(session):
    add_user(session, User(id=1, first_name="Vasya"))
    assert get_user_by_id(session, id=1) == schemas.User(id=1, first_name="Vasya")


def test_get_user_by_id(session):
    add_user(session, User(id=1, first_name="Vasya"))
    get_user_by_id(session, id=1)


def test_if_user_exist(session):
    user = User(id=1, first_name="Vasya")
    add_user(session, user)
    assert if_user_exist(session, user)
