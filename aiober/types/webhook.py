from pydantic import BaseModel

class Webhook(BaseModel):
    status: int
    status_message: str = 'ok'
    event_types: list[str]


