from pydantic import ValidationError


class CustomError(Exception):
    pass


class StorageError(CustomError):
    pass


class UserExistError(StorageError):
    pass


class UserNotExistError(StorageError):
    pass
