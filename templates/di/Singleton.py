from typing import Any
from .Injectable import BaseInjector

class Singleton(BaseInjector):
    def __init__(self, type_: Any, *args, **kwargs) -> None:
        self.type_ = type_
        self.args = args
        self.kwargs = kwargs
        self.__instance = None

    @property
    def Instance(self) -> Any:
        if self.__instance is None:
            self.__instance = self.type_(*self.args, **self.kwargs)
        return self.__instance