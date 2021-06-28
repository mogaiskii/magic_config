__all__ = ['SettingType']

import abc


class SettingType(abc.ABC):
    @classmethod
    def parse(cls, str_value):
        raise NotImplementedError

    @classmethod
    def serialize(cls, value):
        raise NotImplementedError

