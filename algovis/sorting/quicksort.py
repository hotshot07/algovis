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
            yield arr
            i = start - 1
            j = stop + 1
            while True:
                while True:
                    i = i + 1
                    if arr[i] >= arr[pivot]:
                        break
                while True:
                    j = j - 1
                    if arr[j] <= arr[pivot]:
                        break
                if i >= j:
                    break
                else:
                    arr[i], arr[j] = arr[j], arr[i]
                    yield arr

            yield arr
            yield from self.quicksort(arr, start, j, choice)
            yield from self.quicksort(arr, j + 1, stop, choice)

    def sort(self):
        A = copy.deepcopy(self.__datalist)
        print(A)
        for i in self.quicksort(A, 0, len(self.__datalist) - 1, "random"):
            print(i)

    def visualize(self, reverse=False, interval=50):
        _vis_list = copy.deepcopy(self.__datalist)

        AnimateAlgorithm("Quick Sort", _vis_list, self.quicksort(_vis_list, 0, len(_vis_list) - 1, "random"), interval)
