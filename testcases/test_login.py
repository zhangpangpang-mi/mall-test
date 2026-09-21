
import allure

from common.request import Request
from config.config import BASE_URL
from common.assert_util import Assert

from api.login_api import LoginApi
from common.assert_util import Assert



@allure.feature("用户模块")
@allure.story("用户登录")


def test_login():

    result = LoginApi.login(
        "admin",
        "macro123"
    )

    Assert.equal(
        result["code"],
        200
    )