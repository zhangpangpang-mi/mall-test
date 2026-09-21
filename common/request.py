import requests
import allure
from common.logger import get_logger
from common.token_util import Token
import time
logger = get_logger()
class Request:

    def get_headers(self):

        token = Token.get_token()

        headers = {}

        if token:
            headers["Authorization"] = (
                    "Bearer " + token
            )

        return headers

    def get(
            self,
            url,
            params=None,
            headers=None,
            retry=3
    ):

        try:

            # 日志
            logger.info("请求方式: GET")
            logger.info(f"请求地址: {url}")
            logger.info(f"请求参数: {params}")
            logger.info(f"请求头: {headers}")

            # Allure附件
            allure.attach(
                "GET",
                "请求方式",
                allure.attachment_type.TEXT
            )

            allure.attach(
                url,
                "请求地址",
                allure.attachment_type.TEXT
            )

            allure.attach(
                str(params),
                "请求参数",
                allure.attachment_type.TEXT
            )

            allure.attach(
                str(headers),
                "请求头",
                allure.attachment_type.TEXT
            )

            if headers is None:
                headers = self.get_headers()

            start_time = time.time()

            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=10
            )

            cost = time.time() - start_time
            logger.info(
                f"接口耗时:{cost:.3f}s"
            )
            allure.attach(
                f"{cost:.3f}s",
                "接口耗时",
                allure.attachment_type.TEXT
            )
            # 响应日志
            logger.info(
                f"响应状态码: {response.status_code}"
            )

            logger.info(
                f"响应结果: {response.text}"
            )

            # Allure响应
            allure.attach(
                str(response.status_code),
                "响应状态码",
                allure.attachment_type.TEXT
            )

            allure.attach(
                response.text,
                "响应结果",
                allure.attachment_type.TEXT
            )

            try:

                return response.json()


            except Exception:

                return response.text


        except Exception as e:

            logger.error(
                f"GET请求失败: {e}"
            )

            allure.attach(
                str(e),
                "异常信息",
                allure.attachment_type.TEXT
            )
            if retry > 1:
                logger.info(
                    f"请求失败，剩余重试次数:{retry - 1}"
                )

                time.sleep(1)

                return self.get(
                    url,
                    params,
                    headers,
                    retry - 1
                )

            raise e

    def post(
            self,
            url,
            data=None,
            params=None,
            headers=None,
            retry=3
    ):

        try:

            # ===== 日志 =====
            logger.info("请求方式: POST")

            logger.info(
                f"请求地址: {url}"
            )

            logger.info(
                f"请求参数: {data}"
            )

            logger.info(
                f"请求头: {headers}"
            )

            # ===== Allure附件 =====

            allure.attach(
                "POST",
                "请求方式",
                allure.attachment_type.TEXT
            )

            allure.attach(
                url,
                "请求地址",
                allure.attachment_type.TEXT
            )

            allure.attach(
                str(data),
                "请求参数",
                allure.attachment_type.TEXT
            )

            allure.attach(
                str(headers),
                "请求头",
                allure.attachment_type.TEXT
            )

            # ===== 发送请求 =====
            if headers is None:
                headers = self.get_headers()

            logger.info(
                f"最终请求头:{headers}"
            )



            start_time = time.time()

            response = requests.post(
                url,
                json=data,
                params=params,
                headers=headers,
                timeout=10
            )

            cost = time.time() - start_time
            logger.info(
                f"接口耗时:{cost:.3f}s"
            )
            allure.attach(
                f"{cost:.3f}s",
                "接口耗时",
                allure.attachment_type.TEXT
            )

            # ===== 响应日志 =====

            logger.info(
                f"响应状态码: {response.status_code}"
            )

            logger.info(
                f"响应结果: {response.text}"
            )

            # ===== Allure响应附件 =====

            allure.attach(
                str(response.status_code),
                "响应状态码",
                allure.attachment_type.TEXT
            )

            allure.attach(
                response.text,
                "响应结果",
                allure.attachment_type.TEXT
            )

            try:

                return response.json()


            except Exception:

                return response.text


        except Exception as e:

            logger.error(
                f"POST请求失败: {e}"
            )

            allure.attach(
                str(e),
                "异常信息",
                allure.attachment_type.TEXT
            )
            if retry > 1:
                logger.info(
                    f"请求失败，剩余重试次数:{retry - 1}"
                )

                time.sleep(1)

                return self.post(
                    url,
                    data,
                    params,
                    headers,
                    retry - 1
                )

            raise e