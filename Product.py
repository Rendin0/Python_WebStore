class Product:
    __counter = 0

    def __init__(self, name, description, price):
        if type(name) != str \
           or type(description) != str \
           or type(price) != float:
            raise ValueError('Имя, описание должно быть str, цена должна быть float')

        self.__id = Product.__counter
        Product.__counter += 1

        self.__name: str = name
        self.__description: str = description
        self.__price: float = price
    
    def get_name(self):
        return self.__name
    def get_description(self):
        return self.__description
    def get_price(self):
        return self.__price
    def get_id(self):
        return self.__id
    
    def __str__(self):
        return f'{{"name": "{self.get_name()}", "description": "{self.get_description()}", "price": {self.get_price()}}}'
    def __repr__(self):
        return self.__str__()