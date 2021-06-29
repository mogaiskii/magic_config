import os
import traceback

from magic_config.field import SettingField
from magic_config.loaders import EnvLoader
from magic_config.manager import BaseSettingsManager
from magic_config.settings_types import BoolType


def test_config_smoke_env_bool():
    os.environ['x'] = 'false'
    os.environ['y'] = 'true'
    os.environ['z'] = '1'
    os.environ['q'] = '0'
    os.environ['w'] = 'abracadabra'

    try:
        class AppConfig(BaseSettingsManager):
            x = SettingField(BoolType)
            y = SettingField(BoolType)
            z = SettingField(BoolType)
            q = SettingField(BoolType)
            w = SettingField(BoolType)

            class Meta:
                loaders = [EnvLoader()]

        config = AppConfig()
        str(config.x)
        str(config.y)
        str(config.z)
        str(config.q)
        str(config.w)

        config.x = True
        config.y = True
        config.z = True
        config.q = True
        config.w = True

        str(config.x)
        str(config.y)
        str(config.z)
        str(config.q)
        str(config.w)

    except Exception as e:
        assert False, traceback.format_exc()


def test_config_smoke_kwargs_env_bool():
    os.environ['x'] = 'false'
    os.environ['y'] = 'false'

    try:
        class AppConfig(BaseSettingsManager):
            x = SettingField(BoolType, env__key='y')
            y = SettingField(BoolType)
            z = SettingField(BoolType)

            class Meta:
                loaders = [EnvLoader()]

        config = AppConfig()
        str(config.x)
        str(config.y)
        str(config.z)

        config.x = True
        config.y = True
        config.z = True

        str(config.x)
        str(config.y)
        str(config.z)

    except Exception as e:
        assert False, traceback.format_exc()
