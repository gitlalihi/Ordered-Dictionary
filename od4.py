#Python program that reverses the order of a given OrderedDict.
from collections import OrderedDict

def reverse_ordered_dict(input_dict):
    reversed_items = sorted(input_dict.items(), reverse=True)
    reversed_dict = OrderedDict(reversed_items)
    return reversed_dict

# Example usage:
if __name__ == "__main__":
    
    my_ordered_dict = OrderedDict([('banana', 3), ('apple', 1), ('orange', 2), ('grape', 4)])
    reversed_dict = reverse_ordered_dict(my_ordered_dict)

    print("Original OrderedDict:")
    print(my_ordered_dict)

    print("\nReversed OrderedDict:")
    print(reversed_dict)