#Write a Python program that creates an OrderedDict and adds some items. Print the OrderedDict contents
from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict()

# Add items
ordered_dict['Laptop'] = 15
ordered_dict['Desktop'] = 40
ordered_dict['Mobile'] = 50

# Print the OrderedDict contents
for item, quantity in ordered_dict.items():
    print(f"Item: {item}, Quantity: {quantity}")