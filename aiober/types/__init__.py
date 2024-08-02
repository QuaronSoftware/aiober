from pydantic import parse_obj_as
from .base import ViberObject

from .keyboard import Keyboard, KeyboardButton
from .massage import Message
from .user import User
from .seen import Seen
from .conversation_started import ConversationStarted
from .subscribed import Subscribed, Unsubscribed
from .rich_media import RichMediaKeyboard
from .webhook import Webhook

__all__ = [
    'Message',
    'User',
    'Seen',
    'ConversationStarted',
    'Subscribed',
    'Unsubscribed',
    'Keyboard',
    'KeyboardButton',
    'RichMediaKeyboard',
    'RMKeyboardButton',
    'parse_object',
    'Webhook'
]

_object: dict[str, ViberObject] = {
    'message': Message,
    'seen': Seen,
    'conversation_started': ConversationStarted,
    'subscribed': Subscribed,
    'unsubscribed': Unsubscribed
}

def parse_object(request_data: dict, bot):
    event: str = request_data.get('event')

    kwargs = {'bot': bot, '_bot': bot}

    data: dict = (
        request_data | kwargs | request_data[event]
        if event == 'message'
        else request_data | kwargs
    )
    if event in data:
        data.pop(event)

    return parse_obj_as(_object[event], data) if event in _object else None

