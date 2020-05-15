from algovis import sorting

my_list = [6, 3, 21, 1, 6, 98, 0, 2]
bs_object = sorting.BubbleSort(my_list)
answer = bs_object.sort(reverse=True)

print(answer)
