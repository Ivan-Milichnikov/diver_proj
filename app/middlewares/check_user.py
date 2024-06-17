from aiogram import BaseMiddleware
from aiogram.types import Message

from app.database.users import User

from typing import Callable,Awaitable,Any,Dict
class CheckInDB(BaseMiddleware):

    async def __call__(self,
        handler: Callable[[Message, Dict[str,Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        member = event.from_user.id
        #res = User().check_user(member)
        if member in [1466659409,658773631]:
            return await handler(event,data)

