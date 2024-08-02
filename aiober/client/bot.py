
from .session.base import BaseSession
from aiober.types import Keyboard, RichMediaKeyboard
from aiober.methods.base import ViberMethod
from aiober.client.session.request import AiohttpSession


class Bot:
    def __init__(
            self,
            token: str,
            session: BaseSession = None
    ):
        self._token = token
        self.session = session if isinstance(session, BaseSession) else AiohttpSession()
    
    @property
    def token(self):
        return self._token

    async def __call__(self, method: ViberMethod, request_runtime: int = None):
        return await self.session(self, method, timeout=request_runtime)
    
    def send_message(self, chat_id: str, text: str, keyboard: Keyboard = None):
        from aiober.methods import SendMessage

        return SendMessage(
            chat_id,
            type='text',
            text=text,
            keyboard=keyboard
        ).as_(self)
    
    def send_rich_media(self, chat_id: str, rich_media: RichMediaKeyboard):
        from aiober.methods import SendMessage

        return SendMessage(
            chat_id,
            type='rich_media',
            text=None,
            rich_media=rich_media
        ).as_(self)
