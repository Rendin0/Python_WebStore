from Product import Product

class ProductsList:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, name, description, price):
        product = Product(name, description, price)
        self.__products.append(product)
        return product

    def add_existing_product(self, product):
        if type(product) != Product:
            raise ValueError('Необходимо передать Product')
        self.__products.append(product)
    
    def get_products(self):
        return self.__products

    def remove_product(self, id):
        if type(id) != int:
            raise ValueError('id должен быть типа int')
        
        for product in self.__products:
            if product.get_id() == id:
                self.__products.remove(product)
                break
    
    def __str__(self):
        return self.__products.__str__()
    def __repr__(self):
        return self.__str__()