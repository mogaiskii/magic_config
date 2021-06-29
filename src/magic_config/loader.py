import abc

from magic_config.interfaces import AbstractLoader


class BaseLoader(AbstractLoader, abc.ABC):
    __available_options__ = []

    def __init__(self, **options):
        self._options = dict()

        for k,v  in options.items():
            if k in self.__available_options__:
                self._options[k] = v

    def _get_params(self, **kwargs):
        return {**self._options, **kwargs}
