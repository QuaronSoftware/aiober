
class ViberAPIServer:
    def __init__(self, *, base: str):
        self.base = base

    def get_api_url(self, method: str):
        return self.base.format(method=method)


PRODUCTION = ViberAPIServer(
    base='https://chatapi.viber.com/pa/{method}'
)
