from magic_config.settings_type import SettingType


class StrType(SettingType):

    @classmethod
    def parse(cls, str_value):
        return str_value

    @classmethod
    def serialize(cls, value):
        return str(value)

    @classmethod
    def cast(cls, value):
        return str(value)
