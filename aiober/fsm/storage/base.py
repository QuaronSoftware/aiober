
from typing import Any
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class StorageKey:
    user_id: str
    chat_id: str

class BaseStorage(ABC):
    

    @abstractmethod
    async def set_state(self, key: StorageKey, state: str) -> None:
        """
        Set state for key

        :key: storage key
        :state: new state
        """
        pass
    
    @abstractmethod
    async def get_state(self, key: StorageKey) -> str:
        """
        Get state by storage key
        """

        pass

    @abstractmethod
    async def set_data(self, key: StorageKey, data: dict[str, Any]):
        """
        Set data to storage key
        """

        pass

    @abstractmethod
    async def get_data(self, key: StorageKey) -> dict[str, Any]:
        """
        Get data by key
        """

        pass

    async def update_data(self, key: StorageKey, data: dict[str, Any]):
        """
        Update data by key
        """

        current_data = await self.get_data(key=key)
        current_data.update(data)
        await self.set_data(key=key, data=current_data)
        return current_data.copy()

    @abstractmethod
    async def close(self) -> None:
        """
        Close storage
        """
        pass