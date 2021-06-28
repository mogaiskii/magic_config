__all__ = ['BaseSettingsManager', 'BaseSettingsManagerMeta']

import abc


class BaseSettingsManagerMeta(abc.ABCMeta):
    """
    metaclass for settings manager. sets behaviour of declaring fields.
    """
    pass


class BaseSettingsManager(metaclass=BaseSettingsManagerMeta):
    """
    abstract base class for every setting manager
    """
    pass
