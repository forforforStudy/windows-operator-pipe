"""
复制或者剪切的处理器
"""
import shutil
import os.path as path

from wop_modules.copyacut_processor.copyacut_processor_action import CopyacutProcessorAction
from wop_modules.copyacut_processor.copyacut_processor_config import CopyacutProcessorConfig


class CopyacutProcessor(object):
    def __init__(self, config: CopyacutProcessorConfig):
        self.config = config

    @staticmethod
    def private_copy_execute(from_path: str, to_path: str):
        # from_path is file
        if path.isdir(from_path):
            shutil.copytree(from_path, to_path)
        else:
            shutil.copy(from_path, to_path)

    @staticmethod
    def private_cut_execute(from_path: str, to_path: str):
        shutil.move(from_path, to_path)

    def execute_copy_and_cut(self):
        config = self.config

        from_path = config.from_path
        to_path = config.to_path
        action = config.action

        if action is CopyacutProcessorAction.COPY:
            CopyacutProcessor.private_copy_execute(from_path, to_path)
        elif action is CopyacutProcessorAction.CUT:
            CopyacutProcessor.private_cut_execute(from_path, to_path)
