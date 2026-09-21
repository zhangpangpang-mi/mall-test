from common.variable import Variable


class Extract:


    @staticmethod
    def extract(response, rules):


        for key, path in rules.items():

            value = response


            for field in path.split("."):

                value = value[field]


            Variable.set(
                key,
                value
            )