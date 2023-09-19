from tele_trans import schemas


def test_user():
    schemas.User(id=1, first_name="Vasya")
    schemas.User(id=1, first_name="Vasya", last_name="Ivanov")
    schemas.User(id=1, first_name="Vasya", user_name="vasyacom")
