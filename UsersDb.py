from User import User
from Merchant import Merchant
from hashlib import md5
from Consumer import Consumer
import json


class UsersDb:
    def read_file(path):
        db_dict = ''
        with open(path, 'r', encoding='utf-8') as file:
            db_dict = json.loads(file.readline().replace('\n', ''))
        db = UsersDb()

        for user in db_dict['users']:
            account = db.create_account(user['login'], user['pwd_hash'], user['user_type'])
            for product in user['products']:
                account.add_product_to_list(product['name'], product['description'], product['price'])
        return db


    def __init__(self):
        self.__users: list[User] = []

    def register(self, login, password, user_type):
        pwd_hash = md5(password.encode()).hexdigest()
        return self.create_account(login, pwd_hash, user_type)
    
    def create_account(self, login, pwd_hash, user_type):
        if type(login) != str or type(pwd_hash) != str \
            or type(user_type) != str:
            raise ValueError('Логин, пароль и тип пользователя должны быть str')

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

