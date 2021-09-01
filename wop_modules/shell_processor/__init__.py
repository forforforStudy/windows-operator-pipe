import subprocess
import os
import os.path as path

default_cwd = os.getcwd()


class ShellProcessor(object):

    def __init__(self, cwd: str = default_cwd):
        self._cwd = cwd if path.isabs(cwd) else path.join(default_cwd, cwd)

    def execute(self, cmd: str):
        process = subprocess.Popen(
            cmd,
            shell=True,
            cwd=self._cwd
        )

        process.wait()

        return process
