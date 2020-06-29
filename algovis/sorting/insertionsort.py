"""
Author: Mayank Arora (hotshot07)
"""


from ._base_class import BaseClass
from ._timer import Timer
from ._animation import AnimateAlgorithm
import copy


class InsertionSort(BaseClass):

    def __init__(self, datalist):
        super().__init__(datalist)
        self.__datalist = datalist

    def __repr__(self):
        return f'algovis.sorting.insertionsort.InsertionSort({self.__datalist})'

    def __ascending_sort_algo(self):
        _asc_list = copy.deepcopy(self.__datalist)
        _length_of_list = len(_asc_list)

        for i in range(1, _length_of_list):

            _key = _asc_list[i]
            j = i - 1

            while j>=0 and _key < _asc_list[j]:
                 _asc_list[j+1] = _asc_list[j]
                 j -= 1

            _asc_list[j+1] = _key

            yield _asc_list

    def __descending_sort_algo(self):
        _desc_list = copy.deepcopy(self.__datalist)
        _length_of_list = len(_desc_list)

        for i in range(1, _length_of_list):

            _key = _desc_list[i]
            j = i - 1

            while j>=0 and _key > _desc_list[j]:
                 _desc_list[j+1] = _desc_list[j]
                 j -= 1

            _desc_list[j+1] = _key

            yield _desc_list


    def __sort_it(self, reverse, steps):
        _iteration_dict = {}
        iterations = 0

        if not reverse:
            for _yielded_list in self.__ascending_sort_algo():
                iterations += 1
                _iteration_dict[iterations] = copy.deepcopy(_yielded_list)
        else:
            for _yielded_list in self.__descending_sort_algo():
                iterations += 1
                _iteration_dict[iterations] = copy.deepcopy(_yielded_list)

        if steps:
            print()
            print("Iteration    List")
            for _iter, _list in _iteration_dict.items():
                print("    " + str(_iter) + "        " + str(_list))

            print()
        return _iteration_dict


    def sort(self, reverse=False, steps=False):
        _sorted_object = self.__sort_it(reverse, steps)
        return list(_sorted_object.values())[-1]






        #     for i in range(1, len(arr)):
        #
        # key = arr[i]
        #
        # # Move elements of arr[0..i-1], that are
        # # greater than key, to one position ahead
        # # of their current position
        # j = i-1
        # while j >= 0 and key < arr[j] :
        #         arr[j + 1] = arr[j]
        #         j -= 1
        # arr[j + 1] = key
