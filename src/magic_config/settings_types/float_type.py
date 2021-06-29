from magic_config.settings_type import SettingType


class FloatType(SettingType):

    @classmethod
    def parse(cls, str_value):
        return float(str_value)

    @classmethod
    def serialize(cls, value):
        return str(value)

    @classmethod
    def cast(cls, value):
        return float(value)
