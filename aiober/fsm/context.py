from typing import Any
from .storage.base import BaseStorage, StorageKey

class FSMcontext:
    
    def __init__(self, key: StorageKey, storage: BaseStorage):
        self._storage_key = key
        self._storage = storage
    
    async def get_state(self) -> str:
        return await self._storage.get_state(self._storage_key)

    async def set_state(self, state: str) -> None:
        return await self._storage.set_state(self._storage_key, state=state)
    
    async def get_data(self) -> dict[str, Any]:
        return await self._storage.get_data(self._storage_key)
    
    async def set_data(self, data: dict[str, Any] = {}, **kwargs):
        return await self._storage.set_data(self._storage_key, data | kwargs)

    async def update_data(self, data: dict[str, Any] = {}, **kwargs):
        return await self._storage.update_data(self._storage_key, data | kwargs)
    
    async def clear(self):
        await self.set_state(None)
        await self.set_data({})