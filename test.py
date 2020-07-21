from algovis import sorting
from algovis import searching
import random

my_list = [i + 1 for i in range(100)]

random.shuffle(my_list)

bs = sorting.BubbleSort(my_list)

bs.visualize(interval=100)
