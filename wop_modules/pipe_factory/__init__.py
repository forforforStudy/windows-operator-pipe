import yaml

from typing import List, TypedDict, Callable

from wop_modules.pipe_factory.config_task_const import ConfigActions, ZipConfig, ShellConfig, CopyAndCutConfig
from wop_modules.copyacut_processor import CopyacutProcessor, CopyacutProcessorConfig, CopyacutProcessorAction
from wop_modules.shell_processor import ShellProcessor
from wop_modules.zip_processor import ZipProcessor, ZipProcessorConfig


class TaskShaped(TypedDict):
    action: ConfigActions
    zip_config: ZipConfig
    shell_config: ShellConfig
    copyacut_config: CopyAndCutConfig


class ConfigParserReturn(TypedDict):
    run: Callable[[], List]


class ConfigParser(object):
    def __init__(self, path: str):
        yaml_file = open(path)
        self.yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)

    def parser(self) -> ConfigParserReturn:
        yaml_data = self.yaml_data

        tasks: List[TaskShaped] = yaml_data.get('tasks')
        tasks_processor: List[Callable] = []

        for task in [t for t in tasks if t['action'] in [item.value for item in ConfigActions]]:
            tasks_processor.append(ConfigParser.map_task_to_processor(task))

        return {'run': lambda: [processor() for processor in tasks_processor]}

    @staticmethod
    def map_task_to_processor(task: TaskShaped) -> Callable:
        action = task['action']

        # shell命令行的处理
        if action == ConfigActions.SHELL.value:
            shell_config = task['shell_config']
            return lambda: ShellProcessor(shell_config['cwd']).execute(shell_config['cmd'])
        # copy和cut的处理
        elif action == ConfigActions.COPY_AND_CUT.value:
            copy_and_cut_config = task['copyacut_config']
            return lambda: CopyacutProcessor(
                CopyacutProcessorConfig(
                    action=CopyacutProcessorAction[copy_and_cut_config['action']],
                    from_path=copy_and_cut_config['fro'],
                    to_path=copy_and_cut_config['to'],
                    override=copy_and_cut_config['override']
                )
            ).execute_copy_and_cut()
        # zip处理
        elif action == ConfigActions.ZIP.value:
            zip_config = task['zip_config']
            return lambda: ZipProcessor().execute(
                ZipProcessorConfig(directory_path=zip_config['fro'], zip_target_path=zip_config['to'],
                                   ignore_regexps=zip_config['ignore'])
            )
