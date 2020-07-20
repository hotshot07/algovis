from algovis import sorting
import random

my_list = [i for i in range(100)]

# random.shuffle(my_list)

bs_object = sorting.MergeSort(my_list)

#print(bs_object.sort(pivot="last", reverse=True, steps=True))

# bs_object.sort(pivot="random")

bs_object.visualize(interval=50, reverse=True)
