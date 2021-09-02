import unittest
import os.path as path

from tests.context_util import fixtures_dir, clean_path
from wop_modules.pipe_factory import ConfigParser, ConfigParserReturn, global_context


class PipeFactoryTester(unittest.TestCase):
    config_parser = ConfigParser(
        path.join(
            fixtures_dir,
            'pipe_config.yml'
        )
    )

    @classmethod
    def setUpClass(cls) -> None:
        # 清理测试数据
        clean_path(path.join(fixtures_dir, 'pipe_factory_resources/copy_results'))
        clean_path(path.join(fixtures_dir, 'pipe_factory_resources/results'))

        clean_path(path.join(fixtures_dir, 'pipe_factory_resources'))

    def test_pipe_config_yaml_run(self):
        self.assertTrue(type(PipeFactoryTester.config_parser.yaml_data) is dict)

        try:
            parsed: ConfigParserReturn = PipeFactoryTester.config_parser.parser()
            parsed['run']()
        except (Exception,):
            self.fail('执行错误')
