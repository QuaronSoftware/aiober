from typing import Any

from .user import User
from .base import ViberObject

class Subscribed(ViberObject):
    user: User

    def from_dict(self, request_dict):
        super(Subscribed, self).from_dict(request_dict)

        self.user = User().from_dict(request_dict)

        return self

class Unsubscribed(ViberObject):
    user_id: str

    def from_dict(self, request_dict):
        super(Subscribed, self).from_dict(request_dict)

        self.user_id = request_dict["user_id"]

        return self
