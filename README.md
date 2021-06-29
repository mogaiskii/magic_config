# Magic config - declarative settings with multiple backends

**magic_config** is a library for creating configs, that could take
settings from anywhere with any priorities.

## installation

`pip install magic_config`

## How it would be
Package is now in progress. It would be looking this when ready:

```python
from magic_config import SettingField, BaseSettingsManager
from magic_config.settings_types import BoolType
from magic_config.loaders import SQLAlchemyLoader, EnvLoader, YAMLConfigLoader, PyObjectLoader

from .some_your_code import DBSettings, DBOtherSettings, session, some_config_object 


class AppSettings(BaseSettingsManager):
    analitycs_feature_flag = SettingField(BoolType, sqlalchemy__model=DBOtherSettings, default_value=True)
    finances_feature_flag = SettingField(BoolType)

    class Meta:
        loaders = [
            SQLAlchemyLoader(sqlalchemy__model=DBSettings, sqlalchemy__flush=False),
            EnvLoader(),
            YAMLConfigLoader('configs/main.yaml'),
            PyObjectLoader()
        ]


settings = AppSettings(sqlalchemy__session=session, pyobject__object=some_config_object)

print(settings.finances_feature_flag)
settings.finances_feature_flag = 1  # would be set to the first of loaders

```
