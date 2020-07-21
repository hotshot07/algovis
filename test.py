from algovis import sorting
from algovis import searching
import random

my_list = [random.randint(0, 100) for i in range(200)]


bs = searching.BinarySearch(my_list)

bs.visualize(93)
# bs = sorting.BubbleSort(my_list)

# bs.visualize(reverse=True, interval=50)
