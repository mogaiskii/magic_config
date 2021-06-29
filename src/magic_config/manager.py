__all__ = ['BaseSettingsManager', 'BaseSettingsManagerMeta']

import abc

from .utils import NULL


class BaseSettingsManagerMeta(abc.ABCMeta):
    """
    metaclass for settings manager. sets behaviour of declaring fields.
    """
    pass


class BaseSettingsManager(metaclass=BaseSettingsManagerMeta):
    """
    abstract base class for every setting manager
    """

    def __init__(self, loaders=NULL):
        self._loaders = []
        if hasattr(self.Meta, 'loaders'):
            self._loaders.extend(self.Meta.loaders)
        if loaders is not NULL:
            self._loaders.extend(loaders)
        assert len(loaders) > 0

    def get_loaders(self):
        return self._loaders

    def get_main_loader(self):
        if self._loaders:
            return self._loaders[0]

        return None

    class Meta:
        pass
