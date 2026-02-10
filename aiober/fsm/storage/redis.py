import json
from typing import Any, cast, Mapping
from collections.abc import Callable
from dataclasses import dataclass, field

from redis.asyncio.client import Redis
from redis.asyncio.connection import ConnectionPool
from redis.lock import Lock
from redis.typing import ExpiryT

from aiober.fsm.state import State
from .base import BaseStorage, StorageKey, StateType


_JsonLoads = Callable[..., Any]
_JsonDumps = Callable[..., str]


@dataclass
class MemoryStorageRecord:
    data: dict[str, Any] = field(default_factory=dict)
    state: str = None

class RedisStorage(BaseStorage):
    def __init__(
            self,
            redis: Redis,
            state_ttl: ExpiryT | None = None,
            data_ttl: ExpiryT | None = None,
            json_loads: _JsonLoads = json.loads,
            json_dumps: _JsonDumps = json.dumps,
        ) -> None:
        self.redis = redis
        self.state_ttl = state_ttl
        self.data_ttl = data_ttl
        self.json_loads = json_loads
        self.json_dumps = json_dumps

    @classmethod
    def from_url(cls, url: str, connection_kwargs: dict[str, Any] | None = None, **kwargs) -> Redis:
        if connection_kwargs is None:
            connection_kwargs = {}
        pool = ConnectionPool.from_url(url, **connection_kwargs)
        redis = Redis(connection_pool=pool)
        return cls(redis=redis, **kwargs)

    async def close(self):
        await self.redis.close(close_connection_pool=True)

    async def get_state(self, key: StorageKey) -> str:
        value = await self.redis.get(key.build('state'))
        if isinstance(value, bytes):
            return value.decode('utf-8')
        return cast(str | None, value)
    
    async def set_state(self, key: StorageKey, state: StateType) -> None:
        redis_key = key.build('state')
        if state is None:
            await self.redis.delete(redis_key)
        else:
            await self.redis.set(
                redis_key,
                value=cast(str, state.state if isinstance(state, State) else state),
                ex=self.state_ttl
            )
    
    async def get_data(self, key: StorageKey) -> dict[str, Any]:
        redis_key = key.build('data')
        value = await self.redis.get(redis_key)
        if value is None:
            return {}
        if isinstance(value, bytes):
            return value.decode('utf-8')
        return cast(dict[str, Any], self.json_loads(value))

    async def set_data(self, key: StorageKey, data: Mapping[str, Any]) -> None:
        redis_key = key.build('data')
        if not isinstance(data, dict):
            msg = f"Data must be dict or dict-like object, got {type(data).__name__}"
            raise RuntimeError(msg)
        if not data:
            await self.redis.delete(redis_key)
        else:
            await self.redis.set(
                redis_key,
                cast(str, self.json_dumps(data)),
                ex=self.data_ttl
            )
