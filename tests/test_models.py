from tele_trans import models


def test_user():
    models.User(id=1, first_name="Vasya")
    models.User(id=1, first_name="Vasya", last_name="Ivanov")
    models.User(id=1, first_name="Vasya", user_name="vasyacom")
