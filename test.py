from algovis import sorting
import random
from multiprocessing import Process

my_list = [random.randint(0, 100) for i in range(8)]

#my_list = [1 for x in range(10)]

bs_object1 = sorting.BubbleSort(my_list)

bs_object2 = sorting.SelectionSort(my_list)

bs_object3 = sorting.InsertionSort(my_list)

print(bs_object3.sort(reverse=False, steps=False))
# print(bs_object)
#
#
#ascending_sort = bs_object.sort(reverse = True, steps=True)
#
# descending_sort = bs_object.sort(reverse=True)
#
# print(descending_sort)
#
#evalu_obj = bs_object.evaluate(reverse=True, iterations=2)
#
#print(evalu_obj)
#
