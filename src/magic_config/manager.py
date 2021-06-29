from typing import Dict, Any, Optional

import abc

from magic_config.interfaces import AbstractSettingField, AbstractLoader, AbstractSettingsManager
from magic_config.utils import NULL


_FIELDS_REGISTRY = '_fields_registry'


class BaseSettingsManagerMeta(abc.ABCMeta):
    """
    metaclass for settings manager. sets behaviour of declaring fields.
    """

    def __new__(mcls, name, bases, attrs: Dict[str, Any]):
        fields = []
        for name, field in attrs.items():
            if isinstance(field, AbstractSettingField):
                fields.append(field)

        attrs[_FIELDS_REGISTRY] = fields
        return super().__new__(mcls, name, bases, attrs)


class BaseSettingsManager(AbstractSettingsManager, metaclass=BaseSettingsManagerMeta):
    """
    abstract base class for every setting manager
    """

    def __init__(self, loaders=NULL):
        self._loaders = []

        if self.Meta.loaders:
            self._loaders.extend(self.Meta.loaders)

        if loaders is not NULL:
            self._loaders.extend(loaders)

        assert len(self._loaders) > 0, 'At least one loader is required'
        assert all([isinstance(loader, AbstractLoader) for loader in self._loaders]), \
            'Loaders should be subclass of AbstractLoader'

    def get_loaders(self):
        return self._loaders

    def get_main_loader(self) -> Optional[AbstractLoader]:
        if self._loaders:
            return self._loaders[0]

        return None

    def get_fields(self):
        return getattr(self, _FIELDS_REGISTRY, [])

    class Meta:
        loaders = []
