import os
import re
import time

from zipfile import ZipFile, ZIP_DEFLATED

from wop_modules.zip_processor.zip_processor_config import ZipProcessorConfig


class ZipProcessor(object):
    """
    执行zip压缩运行能力
    """

    def execute(self, config: ZipProcessorConfig):
        zip_target_path = config.zip_target_path
        directory_path = config.directory_path
        ignore_regexps = config.ignore_regexps

        '''
        传入的 ignore_regexps 进行正则的忽略能力
        '''

        def ignore_regexps_re_tester(text: str):
            if ignore_regexps and len(ignore_regexps) > 0:
                for regexp in ignore_regexps:
                    if re.search(regexp, text, re.M) is None:
                        return False

            return True

        # zip压缩文件对象
        zipfile = ZipFile(
            zip_target_path.format(timestamp=str(int(time.time() * 1000))),
            'w',
            compression=ZIP_DEFLATED
        )

        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                zip_filename: str = os.path.join(dirpath, filename)

                if not ignore_regexps_re_tester(zip_filename):
                    zipfile.write(
                        zip_filename,
                        arcname=zip_filename.replace(directory_path, '')
                    )

        zipfile.close()
