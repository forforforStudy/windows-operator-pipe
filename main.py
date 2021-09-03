import os
import sys
import pathlib

from wop_modules.pipe_factory import ConfigParser, ConfigParserReturn

default_config_filename = 'pipe_config.yml'

if __name__ == '__main__':
    config_path = sys.argv[1]

    if config_path is None:
        # 默认路径值
        config_path = str(pathlib.WindowsPath(os.getcwd()).joinpath(default_config_filename))

    if not pathlib.WindowsPath(config_path).exists():
        raise RuntimeError('配置文件路径有误，请检查: {}'.format(config_path))
    else:
        config_parser = ConfigParser

        parsed: ConfigParserReturn = config_parser.parser()
        parsed['run']()
