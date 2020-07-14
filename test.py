from algovis import sorting
import random

my_list = [random.randint(0, 100) for i in range(10)]
print(my_list)
bs_object1 = sorting.BubbleSort(my_list)

# bs_object1.evaluate(iterations=10)

bs_object1.sort(steps=True)

# bs_object1.code()
