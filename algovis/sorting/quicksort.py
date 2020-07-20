from ._base_class import BaseClass
from ._timer import Timer
from ._animation import AnimateAlgorithm
import copy
import random


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

    def choose_pivot(self, arr, start, end, choice):

        if choice == 'first':
            return arr
        elif choice == 'last':
            arr[start], arr[end] = arr[end], arr[start]
            return arr
        elif choice == 'random':
            randpivot = random.randrange(start, end)
            arr[start], arr[randpivot] = arr[randpivot], arr[start]
            return arr
        elif choice == 'middle':
            middle_pivot = start + (end - start) // 2
            arr[start], arr[middle_pivot] = arr[middle_pivot], arr[start]
            return arr
        else:
            return arr

    def quicksort(self, arr, start, stop, choice):
        if start < stop:
            arr = self.choose_pivot(arr, start, stop, choice)

            pivot = start
            elem_pivot = arr[pivot]  # pivot
            i = start + 1  # a variable to memorize where the
            # partition in the array starts from.
            for j in range(start + 1, stop + 1):

                # if the current element is smaller or equal to pivot,
                # shift it to the left side of the partition.
                if arr[j] <= arr[pivot]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i = i + 1
            arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
            pivot = i - 1

            yield elem_pivot, arr[start:stop + 1]
            yield from self.quicksort(arr, start, pivot - 1, choice)
            yield from self.quicksort(arr, pivot + 1, stop, choice)

    def sort(self, pivot="first"):
        A = copy.deepcopy(self.__datalist)
        print(A)
        for i in self.quicksort(A, 0, len(self.__datalist) - 1, pivot):
            print(i)

    def visualize(self, reverse=False, interval=50, pivot="first"):
        _vis_list = copy.deepcopy(self.__datalist)

        AnimateAlgorithm("Quick Sort", _vis_list, self.quicksort(_vis_list, 0, len(_vis_list) - 1, pivot, vis=True), interval)
