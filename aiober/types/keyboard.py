from typing import Any, List
from pydantic import BaseModel

from .color import WHITE


class KeyboardButton(BaseModel):
    Columns: int | None = 6
    Rows: int | None = 1
    BgColor: str | None = WHITE
    BgMediaType: str | None = None
    BgMedia: str | None = None
    BgMediaScaleType: str | None = None
    BgLoop: bool = True
    ActionType: str | None = None
    ActionBody: str | None = ''
    OpenURLType: str | None = None
    OpenURLMediaType: str | None = None
    TextBgGradientColor: str | None = None
    TextShouldFit: str | None = None
    internal_browser: Any = None
    Map: Any = None
    Image: str | None = None
    ImageScaleType: str | None = None
    TextVAlign: str | None = 'middle'
    TextHAlign: str | None = 'center'
    TextPaddings: list[int] = []
    Text: str | None = None
    TextOpacity: int = 100
    TextSize: str | None = 'regular'

class Keyboard(BaseModel):
    Type: str | None = 'keyboard'
    DefaultHeight: bool = False
    Buttons: List["KeyboardButton"] = []

    class Config:
        arbitrary_types_allowed = True

    def model_post_init(self, __context: Any) -> None:
        if __context:
            self.Buttons = [KeyboardButton(**bttn) for bttn in __context.get('Buttons', [])]
    
    def to_json(self):
        return {
            'Type': self.Type,
            'DefaultHeight': self.DefaultHeight,
            'Buttons': [bttn.dict() for bttn in self.Buttons if bttn]
        }

