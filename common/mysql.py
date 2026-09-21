import pymysql

from common.logger import get_logger
import allure


logger = get_logger()
class Mysql:

    def __init__(self):

        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="zybk1102",
            database="mall",
            charset="utf8"
        )
        logger.info("数据库连接成功")

    def query(self, sql):

        try:

            logger.info(
                f"执行SQL: {sql}"
            )

            allure.attach(
                sql,
                "执行SQL",
                allure.attachment_type.TEXT
            )

            cursor = self.conn.cursor(
                pymysql.cursors.DictCursor
            )

            cursor.execute(sql)

            result = cursor.fetchall()

            logger.info(
                f"查询结果: {result}"
            )

            allure.attach(
                str(result),
                "数据库结果",
                allure.attachment_type.TEXT
            )

            cursor.close()

            return result


        except Exception as e:

            logger.error(
                f"SQL执行失败: {e}"
            )

            allure.attach(
                str(e),
                "数据库异常",
                allure.attachment_type.TEXT
            )

            raise e


    def close(self):

        self.conn.close()