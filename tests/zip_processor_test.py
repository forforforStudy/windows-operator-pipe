import time
import unittest
import os.path as path

import wop_modules.zip_processor as zp
import wop_modules.zip_processor.zip_processor_config as zc


class ZipProcessorTester(unittest.TestCase):

    def setUp(self) -> None:
        cur_dir = path.dirname(path.realpath(__file__))
        directory_path = path.join(
            cur_dir,
            'fixtures',
            'zip_processor_resources'
        )

        zip_target_path = path.join(
            cur_dir,
            'fixtures',
            'zip_processor_zips',
            'test-file-{}.zip'.format(time.time())
        )

        self.zip_config = zc.ZipProcessorConfig(
            directory_path=directory_path,
            zip_target_path=zip_target_path
        )

    def test_execute(self):
        zp.ZipProcessor.execute(self.zip_config)

        self.assertTrue(path.exists(self.zip_config.zip_target_path))
