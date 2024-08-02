from typing import Any

from . import User, Keyboard
from .base import ViberObject

class ConversationStarted(ViberObject):
    type: str | None = None
    context: str | None = None
    user: User | None = None
    subscribed: bool | None = None

    _bot: Any | None = None

    def model_post_init(self, __context):

        self.user = (
            User(**__context.get('user'))
            if __context
            else self.user
        )

        super().model_post_init(__context)

    def answer(self, text: str, keyboard: Keyboard = None, rich_media = None):
        from aiober.methods import SendMessage

        return SendMessage(
            receiver=self.user.id,
            type=self.type if not rich_media else 'rich_media',
            text=text,
            keyboard=keyboard,
            rich_media=rich_media,
            lat=None,
            lon=None,
            sticker_id=None
        ).as_(self._bot)
    
