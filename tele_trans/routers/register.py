from aiogram import Router
from aiogram.filters import Command
from aiogram.filters import CommandObject
from aiogram.types import Message, User as TgUser

register_router = Router()
from ..database import add_user, get_db
from ..schemas import User
from enum import Enum, auto
from ..exceptions import ValidationError
from loguru import logger


class Commands(Enum):
    new = "new"


@register_router.message(Command(Commands.new.value))
async def new_user(message: Message, command: CommandObject):
    match message:
        case Message(
            from_user=TgUser(
                username=username,
                first_name=first_name,
                last_name=last_name,
                id=user_id,
            )
        ):
            try:
                user = User(first_name=first_name, last_name=last_name, id=user_id)
            except ValidationError as exp:
                logger.exception(exp)
                return
            db = get_db()
            add_user(db, user)

        case _:
            return
