from typing import Any
from aiober.types import Message, Seen
from aiober.fsm.context import FSMcontext

from .base import BaseFilter


class StateFilter(BaseFilter):
    def __init__(self, *state: str):
        self.states = state
    
    async def __call__(self, event: Any, state: FSMcontext):
        state_name = await state.get_state()
        return state_name in self.states
