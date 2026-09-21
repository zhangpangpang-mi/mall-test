import allure

from common.request import Request
from config.config import BASE_URL


class LoginApi:


    @staticmethod
    @allure.step("用户登录")
    def login(username, password):


        url = BASE_URL + "/admin/login"


        data = {
            "username": username,
            "password": password
        }


        return Request().post(
            url,
            data=data
        )