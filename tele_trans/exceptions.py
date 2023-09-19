from pydantic import ValidationError


class CustomError(Exception):
    pass


class StorageError(CustomError):
    pass
