#Python function that creates an OrderedDict and removes a key-value pair from the OrderedDict using a given key.
from collections import OrderedDict

od = OrderedDict([
    ('oranges', 40),
    ('apples', 45),
    ('kiwi', 35),
    ('mangoes', 25)
])

def remove_key_from_ordered_dict(od, key_to_remove):
    if key_to_remove in od:
        del od[key_to_remove]
        print(f"Key '{key_to_remove}' removed successfully.")
    else:
        print(f"Key '{key_to_remove}' not found in the OrderedDict.")




print("Original OrderedDict: ",od)

print("\nKey to remove: 'oranges'")
key_to_remove = 'oranges'
remove_key_from_ordered_dict(od, key_to_remove)


print("\nUpdated OrderedDict: ",od)