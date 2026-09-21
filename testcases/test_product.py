from common.request import Request
from config.config import BASE_URL
import pytest
import allure
from common.yaml_util import read_yaml
from common.assert_util import Assert

from common.excel_util import read_excel
from api.product_api import ProductApi

product_data = read_excel(
    "data/product.xlsx"
)

@allure.feature("商品模块")
@allure.story("商品列表查询")
@pytest.mark.parametrize(
    "data",
    product_data
)
def test_product_list(token,data):


    result = ProductApi.list(
        data["keyword"]
    )

    Assert.equal(
        result["code"],
        data["expect_code"]
    )