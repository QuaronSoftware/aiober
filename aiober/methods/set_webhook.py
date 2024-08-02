from .base import ViberMethod

from .methods import SET_WEBHOOK

from ..types import Webhook


class SetWebhook(ViberMethod[Webhook]):

    __returing__   = Webhook
    __api_method__ = SET_WEBHOOK

    url: str
    event_types: list[str]
    send_name: bool = True
    send_photo: bool = True

    def __init__(
            self,
            url: str,
            event_types: list[str] = [
                                "subscribed",
                                "unsubscribed",
                                "conversation_started",
                                "delivered",
                                "failed",
                                "message",
                                "seen"
                            ],
            send_name: bool = True,
            send_photo: bool = True
    ) -> None:
        super().__init__(
            url=url,
            event_types=event_types,
            send_name=send_name,
            send_photo=send_photo
        )
