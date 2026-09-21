import allure
import time

from api.product_api import ProductApi
from common.assert_util import Assert
from common.variable import Variable
from common.yaml_util import read_yaml

from common.mysql import Mysql
@allure.feature("商品模块")
@allure.story("商品创建-更新-删除完整流程")
def test_product_create_flow(
    token,
    cleanup_product
):


    # 商品名称
    keyword = f"自动化测试商品_{int(time.time())}"


    # ======================
    # 1. 创建商品
    # ======================

    product_data = read_yaml(
        "data/product.yaml"
    )["product"]


    product_data["name"] = keyword


    create_result = ProductApi.create(
        product_data
    )

    allure.attach(
        str(product_data),
        "创建商品数据",
        allure.attachment_type.TEXT
    )
    Assert.equal(
        create_result["code"],
        200
    )



    # ======================
    # 2. 查询商品列表
    # ======================

    list_result = ProductApi.list(
        keyword
    )


    Assert.equal(
        list_result["code"],
        200
    )


    products = list_result["data"]["list"]


    assert len(products) > 0



    # ======================
    # 3. 根据名称找到创建的商品id
    # ======================

    product_id = None


    for product in products:

        if product["name"] == keyword:

            product_id = product["id"]

            break


    assert product_id is not None



    # 保存商品id

    Variable.set(
        "product_id",
        product_id
    )



    # ======================
    # 4. 获取商品编辑信息
    # ======================

    info_result = ProductApi.update_info(
        product_id
    )


    Assert.equal(
        info_result["code"],
        200
    )


    assert info_result["data"]["name"] == keyword



    # ======================
    # 5. 更新商品
    # ======================

    update_data = product_data.copy()


    update_data["id"] = product_id

    update_data["name"] = keyword + "_修改"

    update_data["price"] = 199

    update_data["stock"] = 200



    update_result = ProductApi.update(
        product_id,
        update_data
    )

    allure.attach(
        str(update_data),
        "更新商品数据",
        allure.attachment_type.TEXT
    )
    Assert.equal(
        update_result["code"],
        200
    )



    # ======================
    # 6. 删除商品
    # ======================

    delete_result = ProductApi.update_delete_status(
        product_id,
        1
    )


    Assert.equal(
        delete_result["code"],
        200
    )
    db = Mysql()

    result = db.query(
        f"""
        select delete_status
        from pms_product
        where id={product_id}
        """
    )
    allure.attach(
        str(result),
        "数据库查询结果",
        allure.attachment_type.TEXT
    )

    assert result[0]["delete_status"] == 1

    db.close()