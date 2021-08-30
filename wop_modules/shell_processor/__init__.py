import subprocess
import os

default_cwd = os.getcwd()


class ShellProcessor(object):

    def __init__(self, cwd: str = default_cwd):
        self._cwd = cwd

    def execute(self, cmd: str):
        process = subprocess.Popen(
            cmd,
            shell=True,
            cwd=self._cwd
        )

        process.wait()

        return process
