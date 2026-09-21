import allure


class Assert:


    @staticmethod
    def equal(actual, expected):

        allure.attach(
            str(actual),
            "实际结果",
            allure.attachment_type.TEXT
        )

        allure.attach(
            str(expected),
            "期望结果",
            allure.attachment_type.TEXT
        )


        assert actual == expected, (
            f"实际结果:{actual}, "
            f"期望结果:{expected}"
        )