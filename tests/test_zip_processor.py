import os
import time
import unittest
import os.path as path

import wop_modules.zip_processor as zp
import wop_modules.zip_processor.zip_processor_config as zc
import context_util


class ZipProcessorTester(unittest.TestCase):
    cur_dir = context_util.cur_dir

    zip_resource_temp_filepath = path.join(context_util.fixtures_dir, 'zip_processor_zips')

    @classmethod
    def setUpClass(cls) -> None:
        # 不存在目录时，创建目录
        zip_resource_temp_filepath = ZipProcessorTester.zip_resource_temp_filepath
        if not path.exists(zip_resource_temp_filepath):
            os.mkdir(zip_resource_temp_filepath)

        # 清空 zip_resource_temp_filepath 目录下的文件
        for zip_file in os.listdir(zip_resource_temp_filepath):
            os.remove(path.join(zip_resource_temp_filepath, zip_file))

    def setUp(self) -> None:
        directory_path = path.join(
            ZipProcessorTester.cur_dir,
            'fixtures',
            'zip_processor_resources'
        )

        zip_target_path = path.join(
            ZipProcessorTester.zip_resource_temp_filepath,
            'test-file-{}.zip'.format(time.time())
        )

        self.zip_config = zc.ZipProcessorConfig(
            directory_path=directory_path,
            zip_target_path=zip_target_path,
            ignore_regexps=[]
        )

    def test_execute(self):
        zp.ZipProcessor().execute(self.zip_config)

        self.assertTrue(path.exists(self.zip_config.zip_target_path))
