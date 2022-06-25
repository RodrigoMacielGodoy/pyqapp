from typing import Any
from .Factory import Factory
from .Singleton import Singleton

class DependencyContainer(object):
    _container = {}
    _types = {}

    @staticmethod
    def Factory(type_, name, *args, **kwargs) -> None:
        if name not in DependencyContainer._container:
            DependencyContainer._container[name] = Factory(type_, *args, **kwargs)

    @staticmethod
    def Singleton(type_, name, *args, **kwargs) -> None:
        if name not in DependencyContainer._container:
            DependencyContainer._container[name] = Singleton(type_, *args, **kwargs)

    def __class_getitem__(self, key) -> Any:
        try:
            return DependencyContainer._container[key].Instance
        except KeyError:
            return None

    @staticmethod
    def items() -> list[tuple]:
        return DependencyContainer._container.items()
