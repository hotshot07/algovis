from algovis import sorting
import random

my_list = [random.randint(0, 100) for i in range(20)]

#my_list = [1 for x in range(10)]

bs_object1 = sorting.BubbleSort(my_list)

bs_object1.sort(steps=True)
#
# bs_object2 = sorting.SelectionSort(my_list)
#
# bs_object3 = sorting.InsertionSort(my_list)

# bs_object4 = sorting.MergeSort(my_list)

# bs_object4.visualize(interval=100)

#print(bs_object3.sort(reverse=False, steps=False))


# print(bs_object3)
#
#
#ascending_sort = bs_object3.sort(reverse = True, steps=True)
#
#descending_sort = bs_object3.sort(reverse=True)
#
# print(descending_sort)
#
#evalu_obj = bs_object3.evaluate(reverse=False, iterations=100)
#
# print(evalu_obj)

# bs_object3.visualize()
