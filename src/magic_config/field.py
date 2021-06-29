from typing import Type

__all__ = ['SettingField']

from magic_config.utils import NULL
from magic_config.interfaces import AbstractSettingField, AbstractSettingType, AbstractSettingsManager


class SettingField(AbstractSettingField):

    def __init__(self, type_: Type[AbstractSettingType], name=NULL, default_value=NULL, **loaders_kwargs):
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
        self._loaders_kwargs = loaders_kwargs

    def __set_name__(self, owner, name):
        assert isinstance(owner, AbstractSettingsManager) or issubclass(owner, AbstractSettingsManager)
        self._name = name

    def __get__(self, instance, owner_cls):
        assert isinstance(instance, AbstractSettingsManager)
        return self._load_value(instance)

    def __set__(self, instance, value):
        assert isinstance(instance, AbstractSettingsManager)
        self._set_value(instance, value)

    def _load_value(self, instance: AbstractSettingsManager):
        loaders = instance.get_loaders()
        value = NULL
        for loader in loaders:
            value = loader.get_value(self._name, **self._loaders_kwargs)
            if value is not NULL:
                break

        if value is NULL:
            value = self._default_value

        return self._type.parse(value)

    def _set_value(self, instance: AbstractSettingsManager, value):
        loader = instance.get_main_loader()
        casted_value = self._type.cast(value)
        serialized_value = self._type.serialize(casted_value)
        if loader:
            loader.set_value(self._name, serialized_value, **self._loaders_kwargs)
