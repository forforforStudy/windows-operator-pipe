import os
import os.path as path

cur_dir = path.dirname(path.realpath(__file__))

fixtures_dir = path.join(cur_dir, 'fixtures')


def clean_path(target_path: str) -> None:
    if path.isdir(target_path):
        for real_file_path in [path.join(target_path, file_name) for file_name in os.listdir(target_path)]:
            if path.isfile(real_file_path):
                os.remove(real_file_path)
