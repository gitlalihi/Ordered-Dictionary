#Python program that creates an OrderedDict and populates it with random integer values as values and their ASCII characters as keys. Print the OrderedDict.
from collections import OrderedDict
import random
def random_ascii():
    return chr(random.randint(65,90))
def main():
    od=OrderedDict()
    num= int(input("Enter your range you want to find the values:"))
    for i in range(num):
       key=random_ascii()
       value=random.randint(1,50)
       od[key] =value
    print("\nOrdered Dictionary is" , od)
if __name__=='__main__':
    main()       
    