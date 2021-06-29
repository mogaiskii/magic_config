from magic_config.settings_type import SettingType


class BoolType(SettingType):

    @classmethod
    def cast(cls, value):
        return bool(value)

    @classmethod
    def parse(cls, str_value):
        return str_value.lower()[:1] in ['t', '1']

    @classmethod
    def serialize(cls, value):
        return str(value).lower()
