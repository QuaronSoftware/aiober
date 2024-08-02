import ssl
import certifi
import json

from aiohttp import ClientSession, TCPConnector, FormData
from typing import TypeVar

from aiober.methods.base import ViberMethod

from .base import BaseSession

T = TypeVar('T')


class AiohttpSession(BaseSession):
    def __init__(self):
        self._session: ClientSession = None
        super().__init__()
    
    async def create_session(self, token: str) -> ClientSession:
        if self._session is None:
            self._session = ClientSession(
                connector=TCPConnector(ssl=ssl.create_default_context(cafile=certifi.where())),
                headers={
                    "X-Viber-Auth-Token": token
                }
            )
        
        return self._session

    def build_form_data(self, data: dict) -> dict:
        result = {
            'min_api_version': 2
        }

        for key, value in data.items():
            if value:
                result[key] = value

        return result

    async def make_request(self, bot, method: ViberMethod, timeout: int = None):
        session = await self.create_session(bot.token)

        url = self.api.get_api_url(method.__api_method__)
        form_data = self.build_form_data(method.dict())

        try:
            async with session.post(
                url, data=json.dumps(form_data), timeout=self.timeout if timeout is None else timeout
            ) as resp:
                raw_result = await resp.text()
        except RuntimeError:
            raise RuntimeError()
        except Exception as E:
            raise E

        response = self.check_response(bot, resp.status, raw_result)

        return response.status

    async def __call__(self, bot, method: ViberMethod[T], timeout: int = None):

        await self.make_request(bot, method, timeout)

