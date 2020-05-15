from algovis import sorting

my_list = [1, 1, 1, 1, 1, 1, 1, 1]
bs_object = sorting.BubbleSort(my_list)
#answer = bs_object.sort(iterations=True)

p = bs_object.evaluate(reverse=False, iterations=10)

print(p)
