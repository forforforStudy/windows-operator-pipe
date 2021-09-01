import os

import yaml
import os.path as path
import pathlib

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
    def __init__(self, config_file_path: str):
        yaml_file = open(config_file_path)

        self.yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)

        yaml_data_root_value = self.yaml_data.get('root')
        cur_cwd = os.getcwd()

        """
        执行上下文的根路径
        """
        if yaml_data_root_value is None:
            self.root = cur_cwd
        else:
            if path.isabs(yaml_data_root_value):
                self.root = yaml_data_root_value
            else:
                self.root = path.join(cur_cwd, yaml_data_root_value)

    def parser(self) -> ConfigParserReturn:
        yaml_data = self.yaml_data

        tasks: List[TaskShaped] = yaml_data.get('tasks')
        tasks_processor: List[Callable] = []

        for task in [t for t in tasks if t['action'] in [item.value for item in ConfigActions]]:
            tasks_processor.append(self.map_task_to_processor(task))

        return {'run': lambda: [processor() for processor in tasks_processor]}

    def handle_os_path(self, any_path: str):
        if path.isabs(any_path):
            return any_path
        else:
            return str(pathlib.WindowsPath(self.root).joinpath(any_path))

    def map_task_to_processor(self, task: TaskShaped) -> Callable:
        action = task['action']

        # shell命令行的处理
        if action == ConfigActions.SHELL.value:
            shell_config = task['shell_config']
            return lambda: ShellProcessor(self.handle_os_path(shell_config['cwd'])).execute(shell_config['cmd'])

        # copy和cut的处理
        elif action == ConfigActions.COPY_AND_CUT.value:
            copy_and_cut_config = task['copyacut_config']
            copyacut_action = copy_and_cut_config['action']

            return lambda: CopyacutProcessor(
                CopyacutProcessorConfig(
                    action=CopyacutProcessorAction(copyacut_action),
                    from_path=self.handle_os_path(copy_and_cut_config['fro']),
                    to_path=self.handle_os_path(copy_and_cut_config['to']),
                    override=copy_and_cut_config['override'] == 'true'
                )
            ).execute_copy_and_cut()

        # zip处理
        elif action == ConfigActions.ZIP.value:
            zip_config = task['zip_config']
            return lambda: ZipProcessor().execute(
                ZipProcessorConfig(directory_path=self.handle_os_path(zip_config['fro']),
                                   zip_target_path=self.handle_os_path(zip_config['to']),
                                   ignore_regexps=zip_config['ignore'])
            )
