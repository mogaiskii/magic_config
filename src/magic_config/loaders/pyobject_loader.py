from magic_config.loader import BaseLoader


class PyobjectLoader(BaseLoader):

    __available_options__ = ['pyobject__object']
    __loader_name__ = 'pyobject'

    def _get_object(self, pyobject__object=None, **kwargs):
        if pyobject__object:
            return pyobject__object

        return self._options.get('pyobject__object')

    def get_value(self, field_name, pyobject__object=None, **kwargs):
        key = self.get_key(field_name, **kwargs)
        obj = self._get_object(pyobject__object, **kwargs)
        return getattr(obj, key)

    def set_value(self, field_name, value, pyobject__object=None, **kwargs):
        key = self.get_key(field_name, **kwargs)
        obj = self._get_object(pyobject__object, **kwargs)
        setattr(obj, key, value)
