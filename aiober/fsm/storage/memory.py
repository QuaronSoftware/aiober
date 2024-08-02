from typing import Any, DefaultDict
from collections import defaultdict
from dataclasses import dataclass, field

from .base import BaseStorage, StorageKey


@dataclass
class MemoryStorageRecord:
    data: dict[str, Any] = field(default_factory=dict)
    state: str = None

class MemoryStorage(BaseStorage):
    def __init__(self) -> None:
        self.storage: DefaultDict[StorageKey, MemoryStorageRecord] = defaultdict(MemoryStorageRecord)

    async def get_state(self, key: StorageKey) -> str:
        return self.storage[key].state
    
    async def set_state(self, key: StorageKey, state: str) -> None:
        self.storage[key].state = state
    
    async def get_data(self, key: StorageKey) -> dict[str, Any]:
        return self.storage[key].data.copy()
    
    async def set_data(self, key: StorageKey, data: dict[str, Any]):
        self.storage[key].data = data.copy()

    async def close(self) -> None:
        pass