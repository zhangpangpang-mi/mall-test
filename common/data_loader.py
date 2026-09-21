import pytest

from common.yaml_util import read_yaml


def yaml_data(path, key):

    data = read_yaml(path)[key]

    return pytest.mark.parametrize(
        "data",
        data
    )