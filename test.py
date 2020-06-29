from algovis import sorting
import random

my_list = [random.randint(0, 20) for i in range(10)]

#my_list = [1 for x in range(10)]

bs_object = sorting.SelectionSort(my_list)

# print(bs_object)
#
#
ascending_sort = bs_object.sort(reverse = True, steps=True)
#
# descending_sort = bs_object.sort(reverse=True)
#
# print(descending_sort)
#
# evalu_obj = bs_object.evaluate(reverse=False, iterations=1000)
#
# print(evalu_obj)
#
# p = bs_object.visualize()
