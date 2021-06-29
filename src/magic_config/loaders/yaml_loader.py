import yaml

from magic_config.loader import BaseLoader


class YamlLoader(BaseLoader):

    __available_options__ = ['yaml__filepath']
    __loader_name__ = 'yaml'

    def __init__(self, **options):
        if not options.get('is_readonly'):  # readonly by default
            options['is_readonly'] = True

        super(YamlLoader, self).__init__(**options)

        self._yaml_config: dict = {}
        self._yaml_filename: str = None
        if options.get('yaml__filepath'):
            self._yaml_filename = options.get('yaml__filepath')
            self._yaml_config = self._read_file(self._yaml_filename)

    def _read_file(self, filepath):
        with open(filepath, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)

        return content

    def get_value(self, field_name, yaml__filepath=None, yaml_file=None, **kwargs):
        key = self.get_key(field_name, **kwargs)
        content = self._get_content(yaml__filepath, **kwargs)
        return content.get(key)

    def set_value(self, field_name, value, yaml__filepath=None, yaml__file=None, **kwargs):
        key = self.get_key(field_name, **kwargs)
        content = self._get_content(yaml__filepath, **kwargs)
        content[key] = value

        if yaml__file is not None:
            yaml.safe_dump(content, yaml__file)

        filepath = yaml__filepath or self._yaml_filename

        if filepath:
            with open(filepath, 'w') as yaml_file:
                yaml.safe_dump(content, yaml_file)

    def _get_content(self, yaml__filepath=None, yaml__file=None, **kwargs):
        if yaml__file is not None:
            return yaml.safe_load(yaml__file)

        if yaml__filepath is None or yaml__filepath == self._yaml_filename:
            return self._yaml_config

        if yaml__filepath is not None:
            return self._read_file(yaml__filepath)

        return dict()  # NOTE: Silencing
