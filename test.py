from algovis import sorting
import random

my_list = [random.randint(0, 100) for i in range(10)]

bs_object = sorting.BubbleSort(my_list)

ascending_sort = bs_object.sort(steps=True)

descending_sort = bs_object.sort(reverse=True)

print(descending_sort)

evalu_obj = bs_object.evaluate(reverse=False, iterations=1000)

print(evalu_obj)

#p = bs_object.visualize()
