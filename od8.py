#Python function that takes a list of words and returns an OrderedDict where keys are the words and values are the lengths of the words.
from collections import OrderedDict
def word_lengths_ordered_dict(words):
    ordered_dict = OrderedDict()
    for word in words:
        ordered_dict[word] = len(word)
    return ordered_dict

def main():
    words = ["Red", "Green", "Pink", "White", "Orange"]
    result = word_lengths_ordered_dict(words)
    for word, length in result.items():
        print(f"{word}: {length}")

if __name__ == "__main__":
    main()