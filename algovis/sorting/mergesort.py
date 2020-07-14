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

    def __ascending_sort_merge_algo(self, _passed_list, start, mid, end):
        merged = []
        leftIdx = start
        rightIdx = mid + 1

        while leftIdx <= mid and rightIdx <= end:
            if _passed_list[leftIdx] < _passed_list[rightIdx]:
                merged.append(_passed_list[leftIdx])
                leftIdx += 1
            else:
                merged.append(_passed_list[rightIdx])
                rightIdx += 1

        while leftIdx <= mid:
            merged.append(_passed_list[leftIdx])
            leftIdx += 1

        while rightIdx <= end:
            merged.append(_passed_list[rightIdx])
            rightIdx += 1

        for i, sorted_val in enumerate(merged):
            _passed_list[start + i] = sorted_val

        yield _passed_list

    def _merge_algo(self, _passed_list, start, end):
        if end <= start:
            return

        mid = start + ((end - start + 1) // 2) - 1
        yield from self._merge_algo(_passed_list, start, mid)
        yield from self._merge_algo(_passed_list, mid + 1, end)
        yield from self.__ascending_sort_merge_algo(_passed_list, start, mid, end)
        yield _passed_list

    def _asc_animate_sort_it(self):
        _passed_list = copy.deepcopy(self.__datalist)
        for i in self._merge_algo(_passed_list, 0, len(_passed_list) - 1):
            yield i

    def visualize(self, reverse=False, interval=250):
        _vis_list = copy.deepcopy(self.__datalist)

        if not reverse:
            AnimateAlgorithm("Merge Sort", _vis_list, self._asc_animate_sort_it(), interval)
        else:
            AnimateAlgorithm("Merge Sort", _vis_list, self._descending_sort_algo(), interval)
