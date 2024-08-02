from typing import Any
from pydantic import BaseModel
from .color import WHITE
from .keyboard import KeyboardButton


class RichMediaKeyboard(BaseModel):
    Type: str = 'rich_media'
    ButtonsGroupColumns: int = 6
    ButtonsGroupRows: int = 7
    BgColor: str = WHITE
    Buttons: list[KeyboardButton] = []

    class Config:
        arbitrary_types_allowed = True

    def model_post_init(self, __context: Any) -> None:
        self.Buttons = (
            [KeyboardButton(**data) for data in __context.get('Buttons', [])]
            if __context
            else self.Buttons
        )
    def to_json(self):
        return {
            'Type': self.Type,
            'ButtonsGroupColumns': self.ButtonsGroupColumns,
            'ButtonsGroupRows': self.ButtonsGroupRows,
            'BgColor': self.BgColor,
            'Buttons': [bttn.dict() for bttn in self.Buttons if bttn]
        }