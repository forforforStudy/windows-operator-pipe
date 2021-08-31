from enum import Enum
from typing import List

from wop_modules.copyacut_processor.copyacut_processor_action import CopyacutProcessorAction

"""
yaml_data 的格式为:

tasks:
    -   action: copy_and_cut | shell | zip,
        zip_config:
            fro: str
            to: str
            ignore:
                - .git
        shell_config:
            cmd: str
            cwd: str
        copyacut_config:
            action: cut | copy
            fro: str
            to: str
            override: bool
"""


class ZipConfig(object):
    def __init__(self, fro: str, to: str, ignore: List[str]):
        self.fro = fro
        self.to = to
        self.ignore = ignore


class ShellConfig(object):
    def __init__(self, cmd: str, cwd: str):
        self.cmd = cmd
        self.cwd = cwd


class CopyAndCutConfig(object):
    def __init__(self, action: CopyacutProcessorAction, fro: str, to: str, override: bool):
        self.action = action
        self.fro = fro
        self.to = to
        self.override = override


class ConfigActions(Enum):
    COPY_AND_CUT = 'copy_and_cut'
    SHELL = 'shell'
    ZIP = 'zip'


class ConfigField(Enum):
    ZIP_CONFIG = 'zip_config'
    COPY_AND_CUT_CONFIG = 'copyacut_config'
    SHELL_CONFIG = 'shell_config'
