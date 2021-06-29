import abc

from magic_config.interfaces import AbstractLoader


class BaseLoader(AbstractLoader, abc.ABC):
    __available_options__ = []
    __loader_name__ = ''

    def __init__(self, is_readonly=False, **options):
        self._options = dict(is_readonly=is_readonly)

        for k,v  in options.items():
            if k in self.__available_options__:
                self._options[k] = v

    def _get_params(self, **kwargs):
        return {**self._options, **kwargs}

    def _merge_params(self, **kwargs):
        return {**self._options, **kwargs}

    def get_key(self, field_name, **kwargs):
        params = self._merge_params(**kwargs)
        if params.get(self.__loader_name__ + 'key'):
            return params[self.__loader_name__ + 'key']

        return field_name

    def is_readonly(self):
        return self._options.get('is_readonly')
