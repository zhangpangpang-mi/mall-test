import allure

from common.request import Request
from config.config import BASE_URL


class ProductApi:


    @staticmethod
    @allure.step("查询商品列表")
    def list(keyword):

        url = BASE_URL + "/product/list"

        params = {
            "pageNum": 1,
            "pageSize": 10,
            "keyword": keyword
        }

        return Request().get(
            url,
            params=params
        )


    @staticmethod
    @allure.step("创建商品")
    def create(data):

        url = BASE_URL + "/product/create"


        return Request().post(
            url,
            data=data
        )

    @staticmethod
    @allure.step("更新商品")
    def update(product_id, data):
        url = BASE_URL + f"/product/update/{product_id}"

        return Request().post(
            url,
            data=data
        )

    @staticmethod
    @allure.step("获取商品编辑信息")
    def update_info(product_id):
        url = BASE_URL + f"/product/updateInfo/{product_id}"

        return Request().get(
            url
        )

    @staticmethod
    @allure.step("修改商品删除状态")
    def update_delete_status(product_id, delete_status):
        url = BASE_URL + "/product/update/deleteStatus"

        params = {
            "ids": product_id,
            "deleteStatus": delete_status
        }

        return Request().post(
            url,
            params=params
        )