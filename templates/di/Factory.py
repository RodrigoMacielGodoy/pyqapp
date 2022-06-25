from typing import Any
from .Injectable import BaseInjector

class Factory(BaseInjector):
    def __init__(self, cls: Any, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs
        self.cls = cls

    @property
    def Instance(self) -> Any:
        return self.cls(*self.args, **self.kwargs)