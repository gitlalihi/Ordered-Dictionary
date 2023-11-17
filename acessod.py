#Python program that accesses an item in the OrderedDict by its key. Check if a specified item exists in the OrderedDict as well.
from collections import OrderedDict


ordered_dict = OrderedDict()
ordered_dict['orange'] = 40
ordered_dict['mango'] = 45
ordered_dict['kiwi'] = 35


item = ordered_dict['orange']
print(f"Quantity of oranges: {item}")


item_to_check = 'mango'
if item_to_check in ordered_dict:
    print(f"{item_to_check} exists in the OrderedDict")
else:
    print(f"{item_to_check} does not exist in the OrderedDict")


item_to_check = 'apple'
if item_to_check in ordered_dict:
    print(f"{item_to_check} exists in the OrderedDict")
else:
    print(f"{item_to_check} does not exist in the OrderedDict")
