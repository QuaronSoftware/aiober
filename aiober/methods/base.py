from abc import ABC
from typing import Generic, TypeVar, Any, Generator
from pydantic import BaseModel, ConfigDict

from aiober.client.context_controller import BotContextController

ViberType = TypeVar('ViberType', bound=Any)


class Response(BaseModel):
    status: int
    status_message: str
    message_token: int = None
    chat_hostname: str = None
    billing_status: int = None


class ViberMethod(BotContextController, BaseModel, Generic[ViberType], ABC):
    model_config = ConfigDict(
        extra='allow',
        populate_by_name=True,
        arbitrary_types_allowed=True
    )
    
    async def emit(self, bot) -> ViberType:
        return await bot(self)

    def __await__(self) -> Generator[Any, None, ViberType]:
        if not self._bot:
            raise RuntimeError()
        return self.emit(self._bot).__await__()
