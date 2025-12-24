from Merchant import Merchant
import json
from UsersDb import UsersDb

def main():
    db = UsersDb()

    merchant = db.register('merch1', '3246323', 'merchant')
    cola = merchant.add_product_to_list('Cola', 'drink', 100.0)
    merchant.add_product_to_list('Chocolate', 'eat', 90.0)
    pizza = merchant.add_product_to_list('Pizza', 'tasty eat', 200.0)

    consumer = db.register('consm1', '1wruh', 'consumer')
    consumer.add_item_to_cart(pizza)
    consumer.add_item_to_cart(cola)

    dict1 = json.loads(db.__str__())
    print(json.dumps(dict1, indent=2))

if __name__ == '__main__':
    main()