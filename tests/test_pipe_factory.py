import os
import unittest
import os.path as path

from tests.context_util import fixtures_dir, clean_path
from wop_modules.pipe_factory import ConfigParser, ConfigParserReturn


class PipeFactoryTester(unittest.TestCase):
    config_parser = ConfigParser(
        path.join(
            fixtures_dir,
            'pipe_config.yml'
        )
    )

    resources_root_dir_path = path.join(fixtures_dir, 'pipe_factory_resources')

    zip_result_dir_path = path.join(resources_root_dir_path, 'results')

    copy_result_dir_path = path.join(resources_root_dir_path, 'copy_results')

    @classmethod
    def setUpClass(cls) -> None:
        # 清理测试数据
        for real_path in [cls.resources_root_dir_path, cls.zip_result_dir_path, cls.copy_result_dir_path]:
            clean_path(real_path)

    def test_pipe_config_yaml_run(self):
        self.assertTrue(type(PipeFactoryTester.config_parser.yaml_data) is dict)

        try:
            parsed: ConfigParserReturn = PipeFactoryTester.config_parser.parser()
            parsed['run']()
        except (Exception,):
            self.fail('执行错误')

        '''
        检测 fixtures 
        '''
        self.assertEqual(len(os.listdir(PipeFactoryTester.resources_root_dir_path)), 3)
        self.assertTrue(len(os.listdir(PipeFactoryTester.zip_result_dir_path)) > 0)
        self.assertTrue(len(os.listdir(PipeFactoryTester.copy_result_dir_path)) > 0)
