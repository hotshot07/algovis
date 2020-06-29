"""
Author: Mayank Arora (hotshot07)
"""
from ._base_class import BaseClass
from ._timer import Timer
from ._animation import AnimateAlgorithm
import copy


class SelectionSort(BaseClass):
    def __init__(self, datalist):
        super().__init__(datalist)
        self.__datalist = datalist

    def __repr__(self):
        return f'algovis.sorting.selectionSort.SelectionSort({self.__datalist})'

    def __ascending_sort_algo(self):
        _asc_list = copy.deepcopy(self.__datalist)
        _length_of_list = len(_asc_list)

        for i in range(_length_of_list):
            #minimum unsorted value
            _min_val = _asc_list[i]
            _min_idx = i
            for j in range(i, _length_of_list):
                if _asc_list[j] < _min_val:
                    _min_val = _asc_list[j]
                    _min_idx = j

            _asc_list[i], _asc_list[_min_idx]  = _asc_list[_min_idx], _asc_list[i]
            yield _asc_list

    def __descending_sort_algo(self):
        _asc_list = copy.deepcopy(self.__datalist)
        _length_of_list = len(_asc_list)

        for i in range(_length_of_list):
            #minimum unsorted value
            _max_val = _asc_list[i]
            _max_idx = i
            for j in range(i, _length_of_list):
                if _asc_list[j] > _max_val:
                    _max_val = _asc_list[j]
                    _max_idx = j

            _asc_list[i], _asc_list[_max_idx]  = _asc_list[_max_idx], _asc_list[i]
            yield _asc_list

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
