#Python function that merges two OrderedDict objects. If there are duplicate keys, sum their values. Print the merged OrderedDict.
from collections import OrderedDict

def merge_ordered_dicts(dict1, dict2):
    merged_dict = OrderedDict()

    for key, value in dict1.items():
        merged_dict[key] = merged_dict.get(key, 0) + value

    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value

    return merged_dict

# Example usage:
if __name__ == "__main__":
   
    ordered_dict1 = OrderedDict([('banana', 3), ('apple', 1), ('orange', 2), ('grape', 4)])
    ordered_dict2 = OrderedDict([('apple', 2), ('orange', 5), ('kiwi', 1)])

    
    merged_ordered_dict = merge_ordered_dicts(ordered_dict1, ordered_dict2)

    print("OrderedDict 1:")
    print(ordered_dict1)

    print("\nOrderedDict 2:")
    print(ordered_dict2)

    print("\nMerged OrderedDict (summing values for duplicate keys):")
    print(merged_ordered_dict)