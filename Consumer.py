from User import User
from ProductsList import ProductsList
from Product import Product

class Consumer(User):
    def __init__(self, login, pwd_hash):
        super().__init__(login, pwd_hash)
        self.__cart: ProductsList = ProductsList()
    
    def add_item_to_cart(self, product: Product):
        self.__cart.add_existing_product(product)
    
    def remove_item_from_cart(self, id):
        self.__cart.remove_product(id)

    def get_cart(self):
        return self.__cart.get_products()
    
    def __str__(self):
        return f'{{"login": "{self.get_login()}", "pwd_hash": "{self.get_pwd_hash()}", "user_type": "consumer","cart": {self.__cart}}}'
    def __repr__(self):
        return self.__str__()