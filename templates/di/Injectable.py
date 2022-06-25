from typing import Any


class BaseInjector(object):
    @property
    def Instance(self) -> Any:
        raise NotImplementedError()