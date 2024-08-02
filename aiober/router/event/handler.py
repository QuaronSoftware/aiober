from dataclasses import dataclass, field
from typing import Any, Callable

from aiober.filters import BaseFilter


CallbackType = Callable[..., Any]

class HandlerObject:

    def __init__(self, callback: CallbackType, filters: list[BaseFilter]):
        self.callback = callback
        self.filters  = filters


    def _prepare_kwargs(self, kwargs: dict[str, Any], params: tuple) -> dict[str, Any]:
        return {
            k: v for k, v in kwargs.items() if k in params
        }

    async def check_filters(self, *args, **kwargs) -> tuple[bool, Any]:
        for filter in self.filters:
            result = await filter(*args, **self._prepare_kwargs(kwargs, filter.__call__.__code__.co_varnames))

            if not result: return False, None

            if isinstance(result, dict):
                kwargs.update(result)
        
        return True, kwargs
    
    async def call(self, *args, **kwargs) -> bool:
        _call, _kwargs = await self.check_filters(*args, **kwargs)

        if _call:
            await self.callback(*args, **self._prepare_kwargs(kwargs | _kwargs, self.callback.__code__.co_varnames))
            return True

        return False