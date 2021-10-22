'''
Input:
-------
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Output:
-------
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''
from collections import OrderedDict

number_of_items = int(input())
product_price_dict = {}
product_qty_dict = OrderedDict()

for _ in range(number_of_items):
    value = input().split()
    price = int(value[-1])
    product = ' '.join(value[:-1])
    
    if (not product in product_price_dict.keys()):
        product_price_dict[product] = price
    
    if (product in product_qty_dict.keys()):
        product_qty_dict[product] = product_qty_dict[product] + 1
    else:
        product_qty_dict[product] = 1

for product in product_qty_dict:
    print(product, product_qty_dict[product] * product_price_dict[product])
