from .event import EventHandler


class Router:
    sub_routers: list["Router"] = []
    _parent_router = None

    
    def __init__(self, name: str = None):
        self.seen = EventHandler()
        self.failed = EventHandler()
        self.messages = EventHandler()
        self.delivered = EventHandler()
        self.subscribed = EventHandler()
        self.unsubscribed = EventHandler()
        self.conversation_started = EventHandler()

        self._parent_router = None
        self.name = name
        self.sub_routers: list[Router] = []

        self.eventhandlers: dict[str, EventHandler] = {
            "seen": self.seen,
            "failed": self.failed,
            "message": self.messages,
            "delivered": self.delivered,
            "subscribed": self.subscribed,
            "unsubscribed": self.unsubscribed,
            "conversation_started": self.conversation_started
        }
    
    async def trigger(self, _type: str, *args, **kwargs):
        for router in self.eventhandlers.get(_type).handlers:
            result = await router.call(*args, **kwargs)
            if result: return True

    def include_router(self, router: "Router"):
        if router._parent_router is not None:
            raise ValueError(f"Router is already attached to {router._parent_router}")
        
        router._parent_router = self
        self.sub_routers.append(router)
    
    def include_routers(self, *routers: "Router"):

        if routers:
            for router in routers:
                self.include_router(router)




