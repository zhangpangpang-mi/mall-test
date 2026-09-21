import pytest

from common.token_util import Token
from common.request import Request
from common.assert_util import Assert
from config.config import BASE_URL
from common.variable import Variable
from api.product_api import ProductApi


@pytest.fixture(scope="session")
def token():


    token = Token.get_token()


    if token:

        return token



    url = BASE_URL + "/admin/login"


    data = {
        "username": "admin",
        "password": "macro123"
    }


    result = Request().post(
        url,
        data=data
    )


    Assert.equal(
        result["code"],
        200
    )


    token = result["data"]["token"]


    Token.set_token(
        token
    )


    return token
@pytest.fixture(scope="session")
def token():



    token = Token.get_token()


    if token:

        return token


    url = BASE_URL + "/admin/login"


    data = {
        "username":"admin",
        "password":"macro123"
    }


    result = Request().post(
        url,
        data=data
    )

    Assert.equal(
        result["code"],
        200
    )


    token = result["data"]["token"]


    Token.set_token(token)


    return token


@pytest.fixture
def cleanup_product():

    yield


    product_id = Variable.get(
        "product_id"
    )


    if product_id:

        ProductApi.update_delete_status(
            product_id,
            1
        )