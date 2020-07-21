from algovis import sorting
from algovis import searching
import random

my_list = [i + 1 for i in range(20)]


bs = searching.LinearSearch(my_list)

bs.visualize(15, interval=50)
# bs = sorting.BubbleSort(my_list)

# bs.visualize(reverse=True, interval=50)
