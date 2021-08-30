"""
复制或者剪切的处理器
"""
import os
import shutil

from wop_modules.copyacut_processor.copyacut_processor_action import CopyacutProcessorAction
from wop_modules.copyacut_processor.copyacut_processor_config import CopyacutProcessorConfig


class CopyacutProcessor(object):
    def __init__(self, config: CopyacutProcessorConfig):
        self.config = config

    def execute_copy_and_cut(self):
        config = self.config

        from_path = config.from_path
        to_path = config.to_path
        action = config.action

        if action is CopyacutProcessorAction.COPY:
            shutil.copytree(from_path, to_path)
        elif action is CopyacutProcessorAction.CUT:
            os.rename(from_path, to_path)
