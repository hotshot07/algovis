from algovis import __version__


def test_version():
    assert __version__ == '0.1.0001'


from algovis import sorting

my_list = [6, 3, 21, 1, 6, 98, 0, 2]
a = sorting.BubbleSort(my_list)
b = a.sort(reverse=True)

print(b)
