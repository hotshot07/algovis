from algovis import __version__

from algovis import sorting
from algovis import searching


def test_version():
    assert __version__ == '0.2.0'


def test_sorting():
    mylist = [4, 3, 2, 1]
    A = sorting.BubbleSort(mylist)
    assert A.sort() == [1, 2, 3, 4]


def test_searching():
    mylist = [1, 2, 3, 4, 5]
    bs = searching.BinarySearch(mylist)
    assert bs.search(3) is None
