from typing import List


class ZipProcessorConfig(object):

    def __init__(self,
                 directory_path: str,
                 zip_target_path: str,
                 ignore_regexps: List[str] = []
                 ):
        # 需要压缩的目录
        self.directory_path = directory_path
        # 生成的zip压缩文件的目标地址
        self.zip_target_path = zip_target_path
        # 跳过的文件正则数组
        self.ignore_regexps = ignore_regexps
