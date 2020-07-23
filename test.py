from algovis import sorting
from algovis import searching
import random

my_list = [i + 1 for i in range(100)]

bs = searching.BinarySearch(my_list)

ls = searching.LinearSearch(my_list)

help(ls)


# ls.visualize(5, interval=1)
