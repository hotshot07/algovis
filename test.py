from algovis import searching
import random


my_list = [random.randint(0, 10000000) for i in range(200000)]

bs_object1 = searching.LinearSearch(my_list)

# print(my_list)

bs_object1.evaluate(750, iterations=25)

bs_object1.info()

bs_object1.code()
