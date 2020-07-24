from algovis import sorting
#from algovis import searching
import random

my_list = [i + 1 for i in range(1000)]

random.shuffle(my_list)

bs = sorting.BubbleSort(my_list)
iss = sorting.InsertionSort(my_list)
ss = sorting.SelectionSort(my_list)
ms = sorting.MergeSort(my_list)
qs = sorting.QuickSort(my_list)
