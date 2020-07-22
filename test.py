from algovis import sorting
from algovis import searching
import random

my_list = [i + 1 for i in range(10)]

random.shuffle(my_list)

bs = sorting.QuickSort(my_list)

print()
print()

bs.sort(steps=True, reverse=True, pivot="first")

print()
print()
