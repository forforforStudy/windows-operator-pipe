from enum import Enum
from typing import List, TypedDict

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


class ZipConfig(TypedDict):
    fro: str
    to: str
    ignore: List[str]


class ShellConfig(TypedDict):
    cmd: str
    cwd: str


class CopyAndCutConfig(TypedDict):
    action: str
    fro: str
    to: str
    override: bool


class ConfigActions(Enum):
    COPY_AND_CUT = 'copy_and_cut'
    SHELL = 'shell'
    ZIP = 'zip'


class ConfigField(Enum):
    ZIP_CONFIG = 'zip_config'
    COPY_AND_CUT_CONFIG = 'copyacut_config'
    SHELL_CONFIG = 'shell_config'
