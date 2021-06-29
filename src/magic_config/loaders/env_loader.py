import os

from magic_config.loader import BaseLoader


class EnvLoader(BaseLoader):
    __available_options__ = ['env__key']

    def get_key(self, field_name, env__key=None, **kwargs):
        if env__key:
            return env__key

        if self._options.get('env__key'):
            return self._options.get('env__key')

        return field_name

    def get_value(self, field_name, **kwargs):
        key = self.get_key(field_name, **kwargs)
        return os.environ.get(key)

    def set_value(self, field_name, value, **kwargs):
        key = self.get_key(field_name, **kwargs)
        os.environ[key] = value
