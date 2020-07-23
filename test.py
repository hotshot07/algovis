from algovis import sorting
from algovis import searching
import random

my_list = [i + 1 for i in range(100)]

bs = searching.LinearSearch(my_list)

# bs.evaluate(10, iterations=20)

bs.code()
