from ProductsList import ProductsList

class User:
    __counter = 0

    def __init__(self, login, pwd_hash):
        self.__login: str = login
        self.__pwd_hash: str = pwd_hash

        self.__id = User.__counter
        User.__counter =+ 1
        self.__products = ProductsList()
    
    def add_product_to_list(self, name, description, price):
        return self.__products.add_product(name, description, price)
    
    def remove_product(self, id):
        self.__products.remove_product(id)

    def get_products(self):
        return self.__products.get_products()
    
    def get_login(self):
        return self.__login
    def get_pwd_hash(self):
        return self.__pwd_hash
    def get_id(self):
        return self.__id
    
    def __str__(self):
        return f'{{"login": "{self.get_login()}", "pwd_hash": "{self.get_pwd_hash()}", "user_type": "consumer", "products": {self.__products}}}'
    def __repr__(self):
        return self.__str__()
