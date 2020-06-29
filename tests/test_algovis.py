from algovis import __version__
from algovis import sorting


def test_version():
    assert __version__ == '0.1.2'


def test_sorting():
    mylist = [4, 3, 2, 1]
    A = sorting.BubbleSort(mylist)
    assert A.sort() == [1, 2, 3, 4]
