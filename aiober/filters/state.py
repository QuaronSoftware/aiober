from typing import Any, cast
from inspect import isclass
from collections.abc import Sequence
from aiober.fsm.state import State, StatesGroup
from aiober.fsm.context import FSMcontext, StateType

from .base import BaseFilter


class StateFilter(BaseFilter):
    def __init__(self, *state: StateType):
        if not state:
            msg = "At list one state is required"
            raise ValueError(msg)

        self.states = state
    
    async def __call__(self, event: Any, state: FSMcontext) -> bool | dict[str, Any]:
        raw_state = await state.get_state()
        allowed_states = cast(Sequence[StateType], self.states)
        for state in allowed_states:
            if isinstance(state, str) or state is None:
                if state in {'*', raw_state}:
                    return True
            elif isinstance(state, (State, StatesGroup)):
                if state(event, raw_state):
                    return True
            elif isclass(state) and issubclass(state, StatesGroup) and state()(event=event, raw_state=raw_state):
                return True
        return False
