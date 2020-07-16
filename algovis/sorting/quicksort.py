from ._base_class import BaseClass
from ._timer import Timer
from ._animation import AnimateAlgorithm
import copy


def swap(A, i, j):
    """Helper function to swap elements i and j of list A."""

    if i != j:
        A[i], A[j] = A[j], A[i]


class QuickSort(BaseClass):
    def __init__(self, datalist):
        super().__init__(datalist)
        self.__datalist = datalist

    def __repr__(self):
        return f'algovis.sorting.quicksort.QuickSort({self.__datalist})'

    def quicksort(self, start, end):
        A = self.__datalist

        if start >= end:
            return

        pivot = A[end]
        pivotIdx = start

        for i in range(start, end):
            if A[i] < pivot:
                swap(A, i, pivotIdx)
                pivotIdx += 1
                yield A
        swap(A, end, pivotIdx)
        yield A

        yield from self.quicksort(start, pivotIdx - 1)
        yield from self.quicksort(pivotIdx + 1, end)

    def sort(self):
        for i in self.quicksort(0, len(self.__datalist) - 1):
            print(i)

    def visualize(self, reverse=False, interval=100):
        _vis_list = copy.deepcopy(self.__datalist)

        AnimateAlgorithm("Merge Sort", _vis_list, self.quicksort(0, len(_vis_list) - 1), interval)
