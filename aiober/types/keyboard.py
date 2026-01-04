from typing import Any, List, Optional
from pydantic import BaseModel, Field, ConfigDict

from .color import WHITE

def strip_none(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: strip_none(v) for k, v in obj.items() if v is not None}
    if isinstance(obj, list):
        return [strip_none(v) for v in obj if v is not None]
    return obj

class KeyboardButton(BaseModel):
    Columns: int = 6
    Rows: int = 1
    BgColor: str = WHITE

    BgMediaType: Optional[str] = None
    BgMedia: Optional[str] = None
    BgMediaScaleType: Optional[str] = None
    BgLoop: bool = True

    ActionType: Optional[str] = None
    ActionBody: str = ""

    OpenURLType: Optional[str] = None
    OpenURLMediaType: Optional[str] = None

    TextBgGradientColor: Optional[str] = None
    TextShouldFit: Optional[str] = None

    internal_browser: Any = None
    Map: Any = None

    Image: Optional[str] = None
    ImageScaleType: Optional[str] = None

    TextVAlign: str = "middle"
    TextHAlign: str = "center"
    TextPaddings: list[int] = Field(default_factory=list)

    Text: Optional[str] = None
    TextOpacity: int = 100
    TextSize: str = "regular"

    model_config = ConfigDict(
        populate_by_name=True,
        extra="ignore",
    )

    def model_dump(self, **kwargs):
        kwargs.setdefault("exclude_none", True)
        return super().model_dump(**kwargs)

    def model_dump_json(self, **kwargs):
        kwargs.setdefault("exclude_none", True)
        return super().model_dump_json(**kwargs)


class Keyboard(BaseModel):
    Type: str = "keyboard"
    DefaultHeight: bool = False
    Buttons: List[KeyboardButton] = Field(default_factory=list)

    model_config = ConfigDict(
        populate_by_name=True,
        extra="ignore",
        arbitrary_types_allowed=True
    )

    def model_dump(self, **kwargs):
        kwargs.setdefault("exclude_none", True)
        return super().model_dump(**kwargs)

    def model_dump_json(self, **kwargs):
        kwargs.setdefault("exclude_none", True)
        return super().model_dump_json(**kwargs)

    def model_post_init(self, __context: Any) -> None:
        if __context:
            self.Buttons = [KeyboardButton(**bttn) for bttn in __context.get('Buttons', [])]
    
    def to_json(self):
        return strip_none(self.model_dump(exclude_none=True))
