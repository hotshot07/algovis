from algovis import sorting
from algovis import searching
import random

my_list = [i + 1 for i in range(10)]

bs = searching.LinearSearch(my_list)

bs.search(7)
