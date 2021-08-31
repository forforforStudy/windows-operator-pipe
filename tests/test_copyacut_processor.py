import os
import shutil
import unittest
import context_util
import os.path as path

from wop_modules.copyacut_processor import CopyacutProcessor, CopyacutProcessorConfig, CopyacutProcessorAction


class CopyacutProcessorTester(unittest.TestCase):
    copyacut_resource_temp_path = path.join(context_util.fixtures_dir, 'copyacut_processor_resources')

    copyacut_backup_path = path.join(copyacut_resource_temp_path, 'backup_dir')

    copyacut_from_path = path.join(copyacut_resource_temp_path, 'from_dir')

    copyacut_copy_path = path.join(copyacut_resource_temp_path, 'copy_to_dir')

    copyacut_cut_path = path.join(copyacut_resource_temp_path, 'cut_to_dir')

    backup_files = os.listdir(copyacut_backup_path)

    @classmethod
    def setUpClass(cls) -> None:
        CopyacutProcessorTester.backup_files.sort()

        copyacut_cut_path = CopyacutProcessorTester.copyacut_cut_path
        copyacut_copy_path = CopyacutProcessorTester.copyacut_copy_path
        copyacut_from_path = CopyacutProcessorTester.copyacut_from_path

        # clean and rebuild
        for target_path in [copyacut_cut_path, copyacut_copy_path, copyacut_from_path]:
            if path.exists(target_path):
                shutil.rmtree(target_path)
            os.mkdir(target_path)

    def setUp(self) -> None:
        copyacut_from_path = CopyacutProcessorTester.copyacut_from_path

        # 检测如果 from_path 不存在， 直接从 backup 拷贝过来
        if not path.exists(copyacut_from_path):
            shutil.copytree(CopyacutProcessorTester.copyacut_backup_path, copyacut_from_path)
        # 检测如果 from_path 存在，检测其下的文件完整性跟 backup_dir 里的文件目录完整性相同
        else:
            from_dir_files = os.listdir(copyacut_from_path)
            from_dir_files.sort()

            if from_dir_files != CopyacutProcessorTester.backup_files:
                shutil.rmtree(copyacut_from_path)
                shutil.copytree(CopyacutProcessorTester.copyacut_backup_path, copyacut_from_path)

    def test_copy_directory(self):
        # 拷贝目录配置
        copy_dir_config = CopyacutProcessorConfig(
            CopyacutProcessorAction.COPY,
            from_path=CopyacutProcessorTester.copyacut_from_path,
            to_path=CopyacutProcessorTester.copyacut_copy_path
        )

        # 执行拷贝
        copy_processor = CopyacutProcessor(config=copy_dir_config)
        copy_processor.execute_copy_and_cut()

        target_copy_path = path.join(CopyacutProcessorTester.copyacut_copy_path, 'from_dir')

        # 拷贝断言检测
        self.assertTrue(path.exists(target_copy_path))
        self.assertTrue(len(os.listdir(target_copy_path)) > 0)

        # 覆盖模式检测
        copy_dir_config.override = True
        copy_processor.execute_copy_and_cut()

        # 覆盖模式执行检测
        self.assertTrue(path.exists(target_copy_path))
        self.assertTrue(len(os.listdir(target_copy_path)) > 0)

    def test_cut_directory(self):
        # 剪切目录配置
        cut_dir_config = CopyacutProcessorConfig(
            CopyacutProcessorAction.CUT,
            from_path=CopyacutProcessorTester.copyacut_from_path,
            to_path=CopyacutProcessorTester.copyacut_cut_path
        )

        # 执行剪切
        cut_processor = CopyacutProcessor(config=cut_dir_config)
        cut_processor.execute_copy_and_cut()

        # 剪切断言检测
        self.assertTrue(len(os.listdir(cut_dir_config.to_path)) > 0)

        # 覆盖模式检测
        self.setUp()
        cut_dir_config.override = True
        cut_processor.execute_copy_and_cut()

        # 覆盖模式执行检测
        self.assertTrue(len(os.listdir(cut_dir_config.to_path)) > 0)

    def test_copy_file(self):
        copyacut_from_path = CopyacutProcessorTester.copyacut_from_path

        copy_filename = os.listdir(copyacut_from_path)[0]
        from_file_path = path.join(copyacut_from_path, copy_filename)

        copy_file_config = CopyacutProcessorConfig(
            CopyacutProcessorAction.COPY,
            from_path=from_file_path,
            to_path=CopyacutProcessorTester.copyacut_copy_path
        )

        copy_file_processor = CopyacutProcessor(config=copy_file_config)
        copy_file_processor.execute_copy_and_cut()

        # 断言文件拷贝后要存在
        self.assertTrue(
            path.exists(path.join(copy_file_config.to_path, copy_filename))
        )

        # 覆盖模式检测
        copy_file_config.override = True
        copy_file_processor.execute_copy_and_cut()

        # 覆盖模式执行检测
        self.assertTrue(
            path.exists(path.join(copy_file_config.to_path, copy_filename))
        )

    def test_cut_file(self):
        copyacut_from_path = CopyacutProcessorTester.copyacut_from_path
        origin_from_path_files = os.listdir(copyacut_from_path)

        cut_filename = origin_from_path_files[0]

        from_file_path = path.join(copyacut_from_path, cut_filename)

        cut_file_config = CopyacutProcessorConfig(
            CopyacutProcessorAction.CUT,
            from_path=from_file_path,
            to_path=CopyacutProcessorTester.copyacut_cut_path
        )

        cut_file_processor = CopyacutProcessor(config=cut_file_config)
        cut_file_processor.execute_copy_and_cut()

        self.assertTrue(
            path.exists(path.join(cut_file_config.to_path, cut_filename))
        )
        self.assertTrue(
            len(os.listdir(copyacut_from_path)) + 1 == len(origin_from_path_files)
        )

        # 覆盖模式检测
        self.setUp()
        cut_file_config.override = True
        cut_file_processor.execute_copy_and_cut()

        # 覆盖模式执行检测

        self.assertTrue(
            path.exists(path.join(cut_file_config.to_path, cut_filename))
        )
        self.assertTrue(
            len(os.listdir(copyacut_from_path)) + 1 == len(origin_from_path_files)
        )
