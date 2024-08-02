from typing import Optional, Any, TYPE_CHECKING
from typing_extensions import Self
from pydantic import BaseModel, ConfigDict, PrivateAttr

if TYPE_CHECKING:
    from aiober.client.bot import Bot


class ViberObject(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        extra='allow',
        validate_assignment=True,
        populate_by_name=True,
        arbitrary_types_allowed=True,
        defer_build=True
    )

    event: str
    timestamp: int
    chat_hostname: str
    silent: bool = False
    message_token: int = None

    _bot: Optional["Bot"] = PrivateAttr()

    def model_post_init(self, __context: Any) -> None:
        self._bot = self.bot

    def as_(self, bot: Optional["Bot"]) -> Self:
        self._bot = bot
        return self

    @property
    def bot(self) -> Optional['Bot']:

        return self._bot