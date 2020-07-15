from algovis import sorting
import random

my_list = [random.randint(0, 100) for i in range(20)]

bs_object1 = sorting.MergeSort(my_list)

bs_object1.sort(steps=True, reverse=True)

# bs_object1.sort(steps=True)

# bs_object1.code()

# bs_object1.info()
