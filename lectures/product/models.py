from itertools import product
import json


def create_product(
    id_: int, price: int,
    name: str
): 

    product = {
        'id': id_,
        'price': price,
        'name': name,
    }
    
    with open('db.json', 'r+') as file:
        json_data = json.load(file)
        products = json_data.get('products')
        products.append(product)

        # j_d = {
        #     'products': [{'id': 10, 'name': 'bounty', 'price': 49}]
        # }
        json.dump(json_data, file)
create_product(1, 45, 'snickers')
create_product(2, 45, 'bounty')