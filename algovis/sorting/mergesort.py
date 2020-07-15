"""
Author: Mayank Arora (hotshot07)
"""


from ._base_class import BaseClass
from ._timer import Timer
from ._animation import AnimateAlgorithm
import copy


class MergeSort(BaseClass):
    def __init__(self, datalist):
        super().__init__(datalist)
        self.__datalist = datalist

    def __repr__(self):
        return f'algovis.sorting.mergesort.MergeSort({self.__datalist})'

    def __ascending_sort_merge_algo(self, passed_list, start, mid, end):
        merged = []
        leftIdx = start
        rightIdx = mid + 1

        while leftIdx <= mid and rightIdx <= end:
            if passed_list[leftIdx] < passed_list[rightIdx]:
                merged.append(passed_list[leftIdx])
                leftIdx += 1
            else:
                merged.append(passed_list[rightIdx])
                rightIdx += 1

        while leftIdx <= mid:
            merged.append(passed_list[leftIdx])
            leftIdx += 1

        while rightIdx <= end:
            merged.append(passed_list[rightIdx])
            rightIdx += 1

        for i, sorted_val in enumerate(merged):
            passed_list[start + i] = sorted_val

        yield passed_list

    def __descending_sort_merge_algo(self, passed_list, start, mid, end):
        merged = []
        leftIdx = start
        rightIdx = mid + 1

        while leftIdx <= mid and rightIdx <= end:
            if passed_list[leftIdx] > passed_list[rightIdx]:
                merged.append(passed_list[leftIdx])
                leftIdx += 1
            else:
                merged.append(passed_list[rightIdx])
                rightIdx += 1

        while leftIdx <= mid:
            merged.append(passed_list[leftIdx])
            leftIdx += 1

        while rightIdx <= end:
            merged.append(passed_list[rightIdx])
            rightIdx += 1

        for i, sorted_val in enumerate(merged):
            passed_list[start + i] = sorted_val

        yield passed_list

    def __merge_algo(self, passed_list, start, end, reverse):
        if end <= start:
            return

        mid = start + ((end - start + 1) // 2) - 1
        yield from self.__merge_algo(passed_list, start, mid, reverse)
        yield from self.__merge_algo(passed_list, mid + 1, end, reverse)
        if not reverse:
            yield from self.__ascending_sort_merge_algo(passed_list, start, mid, end)
        else:
            yield from self.__descending_sort_merge_algo(passed_list, start, mid, end)
        yield passed_list


    # generator passed to visualize method, yields a list after every iteration
    def __animate_sort_it(self, reverse=False):
        passed_list = copy.deepcopy(self.__datalist)
        for i in self.__merge_algo(passed_list, 0, len(passed_list) - 1, reverse):
            yield i

    def __sort_it(self, reverse, steps):
        passed_list = copy.deepcopy(self.__datalist)
        iteration_dict = {}
        iterations = 0

        # the 0th iteration is basically the passed list
        iteration_dict[iterations] = self.__datalist

        for yielded_list in self.__merge_algo(passed_list, 0, len(passed_list) - 1, reverse):
            iterations += 1
            iteration_dict[iterations] = copy.deepcopy(yielded_list)

        if steps:
            super()._print_steps(iteration_dict)

        return iteration_dict

    # sort method calls __sort_it, which works more or less like the ones in bubble
    # or insertion, the difference being that the reverse option is passed to
    # __merge_algo, which decides based on reverse which generator to call
    # __ascending_sort_merge_algo or __descending_sort_merge_algo
    def sort(self, reverse=False, steps=False):
        _sorted_object = self.__sort_it(reverse, steps)
        return list(_sorted_object.values())[-1]

    # visualize method in quicksort calls __animate_sort_it

    def visualize(self, reverse=False, interval=250):
        _vis_list = copy.deepcopy(self.__datalist)

        AnimateAlgorithm("Merge Sort", _vis_list, self.__animate_sort_it(reverse), interval)
