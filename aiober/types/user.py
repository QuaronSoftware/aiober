from pydantic import BaseModel

class User(BaseModel):
    id: str = None
    name: str = None
    avatar: str = None
    language: str = 'en'
    country: str = None
    api_version: int = 8
