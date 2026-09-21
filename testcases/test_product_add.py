import allure

from api.product_api import ProductApi
from common.assert_util import Assert


@allure.feature("商品模块")
@allure.story("创建商品")
def test_product_create(token):


    data = {

        "brandId": 1,

        "productCategoryId": 1,

        "name": "自动化测试商品001",

        "productSn": "AUTO001",

        "publishStatus": 1,

        "verifyStatus": 1,

        "price": 99,

        "stock": 100

    }


    result = ProductApi.create(
        data
    )


    Assert.equal(
        result["code"],
        200
    )