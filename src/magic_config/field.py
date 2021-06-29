__all__ = ['SettingField']

from .utils import NULL
from .manager import BaseSettingsManager
from .settings_types import SettingType


class SettingField:
    def __init__(self, type_: SettingType, name=NULL, default_value=NULL, **loaders_kwargs):
        """
        :param type_: type of field, should be subclass of SettingType

        :param name: optional - set the name explicit
        :param default_value: optional - set the default value that would be used if none of loader find something
        :param loaders_kwargs: parameters for loaders. should be set as `<loader_name>__<option>=<value>`
            e.g. env__key='SOME_KEY'
        """
        self._type = type_

        self._default_value = NULL
        if default_value is not NULL:
            self._default_value = default_value

        self._name: str = name
        self._current_value = NULL
        self._loaders_kwargs = loaders_kwargs

    def __set_name__(self, owner, name):
        assert isinstance(owner, BaseSettingsManager)
        self._name = name

    def __get__(self, instance, owner_cls):
        assert isinstance(instance, BaseSettingsManager)
        return self._load_value(instance)

    def __set__(self, instance, value):
        assert isinstance(instance, BaseSettingsManager)
        self._set_value(instance, value)

    def _load_value(self, instance: BaseSettingsManager):
        if self._current_value is not NULL:
            return self._current_value

        loaders = instance.get_loaders()
        value = NULL
        for loader in loaders:
            value = loader.get_value(self._name, **self._loaders_kwargs)
            if value is not NULL:
                break

        if value is NULL:
            value = self._default_value

        return self._type.parse(value)

    def _set_value(self, instance: BaseSettingsManager, value):
        loader = instance.get_main_loader()
        if loader:
            loader.set_value(self._name, value, **self._loaders_kwargs)
