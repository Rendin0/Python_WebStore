from User import User
from Merchant import Merchant
from hashlib import md5
from Consumer import Consumer

class UsersDb:
    def __init__(self):
        self.__users: list[User] = []

    def register(self, login, password, user_type):
        if type(login) != str or type(password) != str \
            or type(user_type) != str:
            raise ValueError('Логин, пароль и тип пользователя должны быть str')
        
        pwd_hash = md5(password.encode()).hexdigest()

        match user_type:
            case 'merchant':
                merchant = Merchant(login, pwd_hash)
                self.__users.append(merchant)
                return merchant
            case 'consumer':
                consumer = Consumer(login, pwd_hash)
                self.__users.append(consumer)
                return consumer
    
    def __str__(self):
        return f'{{"users": {self.__users}}}'
