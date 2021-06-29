import os

from magic_config.loader import BaseLoader


class EnvLoader(BaseLoader):
    __available_options__ = ['env__key']
    __loader_name__ = 'env'

    def get_value(self, field_name, **kwargs):
        key = self.get_key(field_name, **kwargs)
        return os.environ.get(key)

    def set_value(self, field_name, value, **kwargs):
        key = self.get_key(field_name, **kwargs)
        os.environ[key] = value
