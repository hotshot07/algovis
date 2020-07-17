from algovis import searching
import random


my_list = [i for i in range(20000)]

bs_object1 = searching.BinarySearch(my_list)

bs_object2 = searching.LinearSearch(my_list)

bs_object1.evaluate(20, iterations=20)

bs_object2.evaluate(20, iterations=20)


# print(my_list)
