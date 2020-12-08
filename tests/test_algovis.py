from algovis import __version__

from algovis import sorting
from algovis import searching


def test_version():
    if __version__ != '0.1.6':
        raise AssertionError


def test_sorting():
    mylist = [4, 3, 2, 1]
    A = sorting.BubbleSort(mylist)
    if A.sort() != [1, 2, 3, 4]:
        raise AssertionError


def test_searching():
    mylist = [1, 2, 3, 4, 5]
    bs = searching.BinarySearch(mylist)
    if bs.search(3) is not None:
        raise AssertionError
