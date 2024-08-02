from typing import Any, Optional, TYPE_CHECKING

from pydantic import BaseModel, PrivateAttr
from typing_extensions import Self

if TYPE_CHECKING:
    from aiober.client.bot import Bot


class BotContextController(BaseModel):
    _bot: Optional["Bot"] = PrivateAttr()


    def as_(self, bot: Optional["Bot"]) -> Self:
        self._bot = bot
        return self

    @property
    def bot(self) -> Optional['Bot']:

        return self._bot