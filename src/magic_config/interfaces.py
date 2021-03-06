"""
Module for resolving circular imports via "interfaces"
"""

import abc


class AbstractSettingsManager(abc.ABC):
    @abc.abstractmethod
    def get_loaders(self): ...

    @abc.abstractmethod
    def get_main_loader(self): ...

    @abc.abstractmethod
    def get_fields(self): ...


class AbstractSettingField(abc.ABC):
    pass


class AbstractLoader(abc.ABC):

    @abc.abstractmethod
    def get_value(self, field_name, **kwargs):
        """
        :param field_name - field meta name
        """
        ...

    @abc.abstractmethod
    def set_value(self, field_name, value, **kwargs):
        """
        :param field_name: field meta name
        :param value: new value
        """
        ...

    @abc.abstractmethod
    def get_key(self, field_name, **kwargs):
        """
        :param field_name: field meta name
        """
        ...

    @abc.abstractmethod
    def is_readonly(self) -> bool: ...


class AbstractSettingType(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def parse(cls, str_value): ...

    @classmethod
    @abc.abstractmethod
    def serialize(cls, value): ...

    @classmethod
    @abc.abstractmethod
    def cast(cls, value):
        """
        cast python value to type
        """
        ...
