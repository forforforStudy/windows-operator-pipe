import unittest

from typing import List

from wop_modules.shell_processor import ShellProcessor


class ShellProcessorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.commands: List[str] = [
            'dir',
            'python -version'
        ]

        self.shell_processor_inst = ShellProcessor()

    def test_shell_cmd_execute(self):
        count = 0

        # noinspection PyBroadException
        try:
            for command in self.commands:
                self.shell_processor_inst.execute(command)
                count = count + 1
        except Exception:
            pass
        finally:
            self.assertEqual(count, len(self.commands))
