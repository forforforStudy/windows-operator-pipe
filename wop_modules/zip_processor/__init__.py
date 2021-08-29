import os

from zipfile import ZipFile, ZIP_DEFLATED

from wop_modules.zip_processor.zip_processor_config import ZipProcessorConfig


class ZipProcessor(object):
    @staticmethod
    def execute(config: ZipProcessorConfig):
        zip_target_path = config.zip_target_path
        directory_path = config.directory_path

        zipfile = ZipFile(
            zip_target_path,
            'w',
            compression=ZIP_DEFLATED
        )

        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                zip_filename: str = os.path.join(dirpath, filename)

                print(zip_filename, dirpath, filename)

                zipfile.write(
                    zip_filename,
                    arcname=zip_filename.replace(directory_path, '')
                )

        zipfile.close()


