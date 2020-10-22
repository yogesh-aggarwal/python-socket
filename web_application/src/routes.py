from mf import Router
from .home.component import HomeComponent


class App(Router):
    def __init__(self):
        super()
        self.routes = [{"path": "", "component": HomeComponent}]
