import allure

from common.request import Request
from common.mysql import Mysql
from config.config import BASE_URL
from common.assert_util import Assert

@allure.feature("商品模块")
@allure.story("商品列表数据库校验")
def test_product_list_db(token):

    # 1. 调接口
    url = BASE_URL + "/product/list"


    params = {
        "pageNum": 1,
        "pageSize": 10,
        "keyword": "小米"
    }


    headers = {
        "Authorization": "Bearer " + token
    }


    result = Request().get(
        url,
        params=params,
        headers=headers
    )


    # 接口校验

    Assert.equal(
        result["code"],
        200
    )
    # 2. 查数据库
    mysql = Mysql()


    sql = """
    select id,name,price,stock
    from pms_product
    where name like '%小米%'
    """


    db_result = mysql.query(sql)


    print(db_result)



    # 数据库校验
    assert len(db_result) > 0


    mysql.close()