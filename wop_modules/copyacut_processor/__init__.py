"""
复制或者剪切的处理器
"""
import os
import shutil
import os.path as path

from wop_modules.copyacut_processor.copyacut_processor_action import CopyacutProcessorAction
from wop_modules.copyacut_processor.copyacut_processor_config import CopyacutProcessorConfig


class CopyacutProcessor(object):
    def __init__(self, config: CopyacutProcessorConfig):
        self.config = config

    @staticmethod
    def override_target_path(override, to_path):
        if override and path.exists(to_path):
            if path.isdir(to_path):
                shutil.rmtree(to_path)
            else:
                os.remove(to_path)

    @staticmethod
    def private_copy_execute(from_path: str, to_path: str, override: bool):
        base_name = path.basename(from_path)
        copy_target_path = path.join(to_path, base_name)

        if path.isdir(from_path):
            # 重写策略确认
            CopyacutProcessor.override_target_path(override, copy_target_path)

            shutil.copytree(from_path, copy_target_path)
        else:
            # 重写策略确认
            CopyacutProcessor.override_target_path(override, copy_target_path)
            shutil.copy(from_path, to_path)

    @staticmethod
    def private_cut_execute(from_path: str, to_path: str, override: bool):
        override_to_path = path.join(to_path, path.basename(from_path))
        CopyacutProcessor.override_target_path(override, override_to_path)

        shutil.move(from_path, to_path)

    def execute_copy_and_cut(self):
        config = self.config

        from_path = config.from_path
        to_path = config.to_path
        action = config.action
        override = config.override

        if action is CopyacutProcessorAction.COPY:
            CopyacutProcessor.private_copy_execute(from_path, to_path, override=override)
        elif action is CopyacutProcessorAction.CUT:
            CopyacutProcessor.private_cut_execute(from_path, to_path, override=override)
