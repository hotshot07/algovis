from algovis import sorting
import random

my_list = [i for i in range(100)]

# random.shuffle(my_list)

bs_object = sorting.BubbleSort(my_list)

# bs_object.visualize(interval=1)

# bs_object.sort(steps=True)

bs_object.visualize(interval=100, reverse=True)
