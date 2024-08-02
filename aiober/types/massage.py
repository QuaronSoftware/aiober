import logging
from typing import Any, TYPE_CHECKING

from .base import ViberObject
from .user import User
from .keyboard import Keyboard

if TYPE_CHECKING:
    from ..methods import SendMessage

class Message(ViberObject):
    receiver: str = None
    text: str = None
    type: str
    sender: User | None
    message_token: int = None
    reply_type: Any = None

    media: str = None
    thumbnail: str = None
    file_name: str = None
    size: int = None
    duration: int = None
    rich_media: Keyboard | None = None
    keyboard: Keyboard | None = None

    lat: float = None
    lon: float = None

    sticker_id: int = None

    def model_post_init(self, __context):

        self.keyboard = (
            Keyboard(**__context.get('keyboard'))
            if __context
            else self.keyboard
        )

        self.sender = (
            User(**__context.get('sender'))
            if __context
            else self.sender
        )

        super().model_post_init(__context)
    
    def answer(self, text: str, keyboard: Keyboard = None, rich_media = None):
        from aiober.methods import SendMessage

        return SendMessage(
            receiver=self.sender.id,
            type=self.type,
            text=text,
            media=None,
            thumbnail=self.media,
            rich_media=rich_media,
            keyboard=keyboard,
            lat=None,
            lon=None,
            sticker_id=None
        ).as_(self._bot)
    
    def answer_picture(self, media: Any, keyboard: Keyboard = None):
        from aiober.methods import SendMessage
        
        return SendMessage(
            receiver=self.sender.id,
            type=self.type,
            text=None,
            media=media,
            thumbnail=media,
            rich_media=self.rich_media,
            keyboard=keyboard,
            lat=None,
            lon=None,
            sticker_id=None
        ).as_(self._bot)

    def copy_to(self, chat_id: str, *, text: str = None, keyboard: Keyboard = None):
        from aiober.methods import SendMessage

        return SendMessage(
            receiver=chat_id,
            type=self.type,
            text=text or self.text,
            media=self.media,
            thumbnail=self.media,
            rich_media=self.rich_media,
            keyboard=keyboard,
            lat=self.lat,
            lon=self.lon,
            sticker_id=self.sticker_id
        ).as_(self._bot)

