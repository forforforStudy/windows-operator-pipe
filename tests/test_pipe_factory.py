import unittest
import os.path as path

from tests.context_util import fixtures_dir
from wop_modules.pipe_factory import ConfigParser, ConfigParserReturn


class PipeFactoryTester(unittest.TestCase):
    config_parser = ConfigParser(
        path.join(
            fixtures_dir,
            'pipe_config.yml'
        )
    )

    def test_pipe_config_yaml_run(self):
        self.assertTrue(type(PipeFactoryTester.config_parser.yaml_data) is dict)

        try:
            parsed: ConfigParserReturn = PipeFactoryTester.config_parser.parser()
            parsed['run']()
        except (Exception,):
            self.fail('执行错误')
