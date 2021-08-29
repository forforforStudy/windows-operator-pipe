import wop_modules.copyacut_processor.copyacut_processor_action as cpa

class CopyacutProcessorConfig(object):

    def __init__(self, action: cpa.CopyacutProcessorAction, from_path: str, to_path: str):
        self.action = action

        self.from_path = from_path
        self.to_path = to_path

    def execute(self):
        from_path = self.from_path
        to_path = self.to_path

