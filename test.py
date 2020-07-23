from algovis import sorting
#from algovis import searching
import random

my_list = [random.randint(0, 1000) for i in range(100)]

bs = sorting.InsertionSort(my_list)

# bs.evaluate(iterations=1000)

help(bs)
# ls.visualize(5, interval=1)
