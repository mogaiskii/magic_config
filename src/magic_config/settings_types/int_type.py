from magic_config.settings_type import SettingType


class IntType(SettingType):

    @classmethod
    def parse(cls, str_value):
        return int(str_value)

    @classmethod
    def serialize(cls, value):
        return str(value)

    @classmethod
    def cast(cls, value):
        return int(value)
