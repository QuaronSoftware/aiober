from aiober.types import Message

from .base import BaseFilter

class TextFilter(BaseFilter):
    def __init__(self, text: str = None):
        self.text = text
    
    async def __call__(self, message: Message):
        return message.text == self.text

class StartsWithFilter(BaseFilter):
    def __init__(self, text: str = None):
        self.text = text
    
    async def __call__(self, message: Message):
        if message.text and message.text.startswith(self.text):
            lens = len(self.text)
            return {
                'text_ends': message.text[lens::]
            }
        return False