class Token:


    token = None


    @classmethod
    def set_token(cls, value):

        cls.token = value



    @classmethod
    def get_token(cls):

        return cls.token