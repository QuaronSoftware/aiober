from typing import Any

from .base import ViberObject

class Seen(ViberObject):
    user_id: str
    udid: Any = None