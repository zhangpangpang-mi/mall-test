import os

from common.excel_util import read_excel
from common.yaml_util import read_yaml


class DataReader:


    @staticmethod
    def read(path):

        # 获取文件后缀
        suffix = os.path.splitext(path)[1]


        if suffix == ".xlsx":

            return read_excel(path)


        elif suffix == ".yaml" or suffix == ".yml":

            return read_yaml(path)


        else:

            raise Exception(
                f"不支持的数据格式:{suffix}"
            )