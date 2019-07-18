import json

def write_order_to_json(**kwargs):
    dict_to_json = kwargs
    print(dict_to_json)
    with open('orders.json', 'w') as file:
        file.write(json.dumps(dict_to_json, indent=4))
    with open('orders.json', 'r') as file:
        print(file.read())

write_order_to_json(item='pen', quantity=20, price=3, buyer='guest', date='01-07-2019')
