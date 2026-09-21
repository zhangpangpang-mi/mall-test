import allure

from api.product_api import ProductApi
from common.variable import Variable
from common.assert_util import Assert


@allure.feature("商品模块")
@allure.story("更新商品")
def test_product_update(token):


    # 获取之前保存的商品id

    product_id = Variable.get(
        "product_id"
    )


    data = {

        "id": product_id,

        "name": "自动化测试商品001修改",

        "price": 199,

        "stock": 200,

        "publishStatus": 1,

        "verifyStatus": 1

    }


    result = ProductApi.update(
        product_id,
        data
    )


    Assert.equal(
        result["code"],
        200
    )