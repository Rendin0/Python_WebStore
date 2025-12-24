from User import User
from ProductsList import ProductsList

class Merchant(User):
    def __init__(self, login, pwd_hash):
        super().__init__(login, pwd_hash)
        self.__products = ProductsList()
    
    def add_product_to_list(self, name, description, price):
        return self.__products.add_product(name, description, price)
    
    def remove_product(self, id):
        self.__products.remove_product(id)

    def get_products(self):
        return self.__products.get_products()

    def __str__(self):
        return f'{{"login": "{self.get_login()}", "pwd_hash": "{self.get_pwd_hash()}", "user_type": "merchant", "products": {self.__products}}}'
    def __repr__(self):
        return self.__str__()