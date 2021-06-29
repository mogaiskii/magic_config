# Magic config - declarative settings with multiple backends

**magic_config** is a library for creating configs, that could take
settings from anywhere with any priorities.

## installation

`pip install magic_config`

## Example

### Basic example:

```python
from magic_config.field import SettingField
from magic_config.manager import BaseSettingsManager
from magic_config.settings_types import BoolType
from magic_config.loaders import EnvLoader, YamlLoader, PyobjectLoader 


class SomeConfigClass:
    def __init__(self, analitycs_feature_flag, finances_feature_flag):
        self.analitycs_feature_flag = analitycs_feature_flag
        self.finances_feature_flag = finances_feature_flag


some_config_object = SomeConfigClass(True, False)


class AppSettings(BaseSettingsManager):
    analitycs_feature_flag = SettingField(BoolType, default_value=True)
    finances_feature_flag = SettingField(BoolType)

    class Meta:
        loaders = [
            EnvLoader(),
            YamlLoader(yaml__filepath='configs/main.yaml'),
            PyobjectLoader()
        ]


settings = AppSettings()

print(settings.finances_feature_flag)
settings.finances_feature_flag = 1  # would be set to the first of loaders

```

### CustomLoader

```python
from magic_config.field import SettingField
from magic_config.manager import BaseSettingsManager
from magic_config.settings_types import BoolType
from magic_config.loader import BaseLoader


# has no sense. just for example:
class StdLoader(BaseLoader):
    __loader_name__ = 'std'
    __available_options__ = ['std__hint']

    def get_value(self, field_name, std__hint: str=None, **kwargs):
        if std__hint:
            return input(std__hint)
        return input()

    def set_value(self, field_name, value, **kwargs):
        print(value)


class AppSettings(BaseSettingsManager):
    analitycs_feature_flag = SettingField(BoolType, default_value=True)

    class Meta:
        loaders = [
            StdLoader()
        ]
```

## TODO:

- [ ] documentation
- [ ] tests
- [ ] settings instance should also take loaders params
- [ ] more loaders - dotenv, json
- [ ] nested settings
- [ ] basic serialization
