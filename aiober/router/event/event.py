from typing import Any, Callable
from aiober.filters import BaseFilter
from .handler import CallbackType, HandlerObject


class EventHandler:
    def __init__(self) -> None:
        self.handlers: list[HandlerObject] = []
    
    def register(self, callback, filters = []):

        self.handlers.append(HandlerObject(callback, filters))
    
    async def trigger(self, *args, **kwargs: Any) -> None:
        """
        handler will be called when all its filters is pass.
        """

        for handler in self.handlers:
            is_called = await handler.call(*args, **kwargs)
            
            if is_called: break

    def __call__(self, *filters: BaseFilter, **kwargs) -> Callable[[CallbackType], CallbackType]:
        """
        Decorator for registering event handlers
        """

        def wrapper(callback: CallbackType) -> CallbackType:
            self.register(callback, filters)
            return callback

        return wrapper
