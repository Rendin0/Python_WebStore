class User:
    __counter = 0

    def __init__(self, login, pwd_hash):
        self.__login: str = login
        self.__pwd_hash: str = pwd_hash

        self.__id = User.__counter
        User.__counter =+ 1
    
    def get_login(self):
        return self.__login
    def get_pwd_hash(self):
        return self.__pwd_hash
    def get_id(self):
        return self.__id
    
    def __str__(self):
        return f'{{"login": "{self.get_login()}", "pwd_hash": "{self.get_pwd_hash()}"}}'
    def __repr__(self):
        return self.__str__()
