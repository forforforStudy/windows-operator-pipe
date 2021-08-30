from typing import List

import os
import shutil
import wop_modules.copyacut_processor.copyacut_processor_action as cpa


class CopyacutProcessorConfig(object):
    def __init__(
            self,
            action: cpa.CopyacutProcessorAction,
            from_path: str,
            to_path: str,
            skip_regexps: List[str] = None
    ):
        self.action = action
        self.from_path = from_path
        self.to_path = to_path
        self.skip_regexps = [] if skip_regexps is None else skip_regexps

    def execute(self):
        from_path = self.from_path
        to_path = self.to_path
        action = self.action

        if action is cpa.CopyacutProcessorAction.COPY:
            shutil.copytree(from_path, to_path)
        elif action is cpa.CopyacutProcessorAction.CUT:
            os.rename(from_path, to_path)
