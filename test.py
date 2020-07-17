from algovis import searching
from algovis import sorting
import random

my_list = [i for i in range(200)]

bs_object1 = searching.BinarySearch(my_list)

bs_object2 = searching.LinearSearch(my_list)

bs_object1.evaluate(193, iterations=20)

bs_object2.evaluate(193, iterations=20)

my_list2 = [random.randint(0, 100) for x in range(100)]

bs_object3 = sorting.BubbleSort(my_list2)

bs_object3.evaluate(iterations=2)

bs_object4 = sorting.MergeSort(my_list2)

bs_object4.evaluate(iterations=2)
# print(my_list)
