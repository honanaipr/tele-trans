from aiogram import Router
from aiogram.filters import Command
from aiogram.filters import CommandObject
from aiogram import types

register_router = Router()
from .. import database
from .. import schemas
from enum import Enum, auto
from ..exceptions import ValidationError
from loguru import logger
from .. import exceptions
from aiogram.utils.i18n import I18n


class Commands(Enum):
    new = "new"
    delete = "delete"


@register_router.message(Command(Commands.new.value))
async def new_user(message: types.Message, command: CommandObject, i18n: I18n):
    _ = i18n.gettext
    match message:
        case types.Message(
            from_user=types.User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                id=user_id,
            )
        ):
            try:
                user = schemas.User(
                    first_name=first_name, last_name=last_name or "", id=user_id
                )
            except ValidationError as exp:
                logger.exception(exp)
                return
            try:
                db = database.get_db()
                database.add_user(db, user)
            except exceptions.UserExistError as exp:
                await message.answer(_("User is already registered"))
                return
            except exceptions.StorageError as exp:
                await message.answer(_("Error"))
                return
            await message.answer(_("The user was added successfully"))
        case _:
            return


@register_router.message(Command(Commands.delete.value))
async def delete_user(message: types.Message, command: CommandObject, i18n: I18n):
    _ = i18n.gettext
    match message:
        case types.Message(
            from_user=types.User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                id=user_id,
            )
        ):
            try:
                user = schemas.User(
                    first_name=first_name, last_name=last_name or "", id=user_id
                )
            except ValidationError as exp:
                logger.exception(exp)
                return
            try:
                db = database.get_db()
                database.delete_user(db, user)
            except exceptions.UserNotExistError as exp:
                await message.answer(_("User is not registered"))
                return
            except exceptions.StorageError as exp:
                await message.answer(_("Error"))
                return
            await message.answer(_("The user was deleted successfully"))
        case _:
            return
