import os
import sys
import pathlib
import argparse

from wop_modules.pipe_factory import ConfigParser, ConfigParserReturn

default_config_filename = 'pipe_config.yml'

if __name__ == '__main__':
    '''
    解析参数
    '''
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-c', '--config', help='输入配置文件的文件路径')
    arg_namespace = arg_parser.parse_args()

    config_path = arg_namespace.config

    if config_path is None:
        # 默认路径值
        config_path = str(pathlib.WindowsPath(os.getcwd()).joinpath(default_config_filename))

    if not pathlib.WindowsPath(config_path).exists():
        raise RuntimeError('配置文件路径有误，请检查: {}'.format(config_path))
    else:
        config_parser = ConfigParser(config_file_path=config_path)

        parsed: ConfigParserReturn = config_parser.parser()
        parsed['run']()
