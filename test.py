from algovis import sorting
import random


my_list = [random.randint(0, 100) for i in range(20)]

bs_object = sorting.BubbleSort(my_list)


# desc_sort = bs_object.sort(steps=True)

# eval_algo0 = bs_object.evaluate(iterations=100)

# vis_algo = bs_object.visualize(reverse=False)

# bs_object.info()

# bs_object.code()

# bs_object1 = searching.BinarySearch(my_list)

# bs_object2 = searching.LinearSearch(my_list)

# bs_object1.evaluate(193, iterations=20)

# bs_object2.evaluate(193, iterations=20)

# my_list2 = [random.randint(0, 100) for x in range(100)]

# bs_object3 = sorting.BubbleSort(my_list2)

# bs_object3.evaluate(iterations=2)

# bs_object4 = sorting.MergeSort(my_list2)

# bs_object4.evaluate(iterations=2)
# # print(my_list)
