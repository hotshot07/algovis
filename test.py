from algovis import searching
import random


my_list = [i for i in range(200)]

bs_object1 = searching.BinarySearch(my_list)

bs_object1.search(19, steps=True)


# print(my_list)
