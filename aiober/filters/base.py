from abc import ABC, abstractmethod


class BaseFilter(ABC):
    
    def __init__(self):
        ...
    
    @abstractmethod
    async def __call__(self, *args, **kwargs):
        pass
    
    
