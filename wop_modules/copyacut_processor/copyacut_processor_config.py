from typing import List

import wop_modules.copyacut_processor.copyacut_processor_action as cpa


class CopyacutProcessorConfig(object):
    def __init__(
            self,
            action: cpa.CopyacutProcessorAction,
            from_path: str,
            to_path: str,
            override: bool = False,
            skip_regexps: List[str] = None
    ):
        self.action = action
        self.from_path = from_path
        self.to_path = to_path
        self.override = override

        self.skip_regexps = [] if skip_regexps is None else skip_regexps

