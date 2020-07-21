from algovis import sorting
import random

my_list = [i for i in range(1000)]


bs = sorting.BubbleSort(my_list)

bs.visualize(reverse=True)
