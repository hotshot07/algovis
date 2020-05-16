from algovis import sorting
import random

my_list = [random.randint(0, 100) for i in range(10)]
bs_object = sorting.BubbleSort(my_list)
#answer = bs_object.sort(iterations=True)

p = bs_object.sort(reverse=False, steps=True)

print(p)
