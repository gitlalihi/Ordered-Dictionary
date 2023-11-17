#Write a Python program that sorts the OrderedDict by its keys. Sort the OrderedDict by its values as well.
from collections import OrderedDict

def sort_ordered_dict_by_keys(input_dict):
    sorted_dict = OrderedDict(sorted(input_dict.items()))
    return sorted_dict

def sort_ordered_dict_by_values(input_dict):
    sorted_dict = OrderedDict(sorted(input_dict.items(), key=lambda x: (x[1], x[0])))
    return sorted_dict


if __name__ == "__main__":
    
    my_ordered_dict = OrderedDict([('banana', 3), ('apple', 1), ('orange', 2), ('grape', 4)])
    sorted_by_keys = sort_ordered_dict_by_keys(my_ordered_dict)
    print("OrderedDict sorted by keys:")
    print(sorted_by_keys)

    
    sorted_by_values = sort_ordered_dict_by_values(my_ordered_dict)
    print("\nOrderedDict sorted by values:")
    print(sorted_by_values)