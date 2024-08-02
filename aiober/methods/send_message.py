from .base import ViberMethod

from .methods import SEND_MESSAGE

from ..types import Message, Keyboard, RichMediaKeyboard


class SendMessage(ViberMethod[Message]):

    __returing__   = Message
    __api_method__ = SEND_MESSAGE

    receiver: str = None
    type: str | None = None
    text: str | None = None
    media: str | None = None
    thumbnail: str | None = None
    file_name: str | None = None
    size: int | None = None
    duration: int | None = None
    rich_media: RichMediaKeyboard | None = None
    keyboard: Keyboard | None = None
    lat: float | None = None
    lon: float | None = None
    sticker_id: int | None = None

    def __init__(
            self,
            receiver: str,
            type: str,
            text: str,
            media: str = None,
            thumbnail: str = None,
            file_name: str = None,
            size: int = None,
            duration: int = None,
            rich_media: RichMediaKeyboard = None,
            keyboard: Keyboard = None,
            lat: float = None,
            lon: float = None,
            sticker_id: int = None
    ) -> None:
        super().__init__(
            receiver=receiver,
            type=type if rich_media is None else 'rich_media',
            text=text,
            media=media,
            thumbnail=thumbnail,
            file_name=file_name,
            size=size,
            duration=duration,
            rich_media=rich_media.to_json() if rich_media is not None else None,
            keyboard=keyboard.dict() if keyboard is not None else None,
            lat=lat,
            lon=lon,
            sticker_id=sticker_id
        )
