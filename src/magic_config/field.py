__all__ = ['SettingField']

from .utils import NULL
from .manager import BaseSettingsManager
from .types import SettingType


class SettingField:
    def __init__(self, type_: SettingType, *, default_value=NULL):
        self._type = type_

        self._default_value = NULL
        if default_value is not NULL:
            self._default_value = default_value

        self._owner: BaseSettingsManager = None
        self._name: str = None
        self._current_value = NULL

    def __set_name__(self, owner, name):
        assert isinstance(owner, BaseSettingsManager)
        self._owner = owner
        self._name = name

    def __get__(self, instance, owner_cls):
        return self._load_value(instance)

    def __set__(self, instance, value):
        self._set_value(instance, value)

    def _load_value(self, instance):
        pass

    def _set_value(self, instance, value):
        pass
