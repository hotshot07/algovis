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


    def __time_eval_asc(self, iterations):
        _time_list = copy.deepcopy(self.__datalist)
        _length_of_list = len(_time_list)
        _timing_list = []

        while iterations:

            timer = Timer()
            timer.start()

            for i in range(_length_of_list):
                #minimum unsorted value
                _min_val = _time_list[i]
                _min_idx = i
                for j in range(i, _length_of_list):
                    if _time_list[j] < _min_val:
                        _min_val = _time_list[j]
                        _min_idx = j

                _time_list[i], _time_list[_min_idx]  = _time_list[_min_idx], _time_list[i]

            stop = timer.stop()
            _timing_list.append(stop)
            iterations -= 1
            _time_list = copy.deepcopy(self.__datalist)

        return _timing_list



    def __time_eval_desc(self, iterations):
        _time_list = copy.deepcopy(self.__datalist)
        _length_of_list = len(_time_list)
        _timing_list = []

        while iterations:

            timer = Timer()
            timer.start()

            for i in range(_length_of_list):
                #minimum unsorted value
                _max_val = _time_list[i]
                _max_idx = i
                for j in range(i, _length_of_list):
                    if _time_list[j] > _max_val:
                        _max_val = _time_list[j]
                        _max_idx = j

                _time_list[i], _time_list[_max_idx]  = _time_list[_max_idx], _time_list[i]

            stop = timer.stop()
            _timing_list.append(stop)
            iterations -= 1
            _time_list = copy.deepcopy(self.__datalist)

        return _timing_list



    def sort(self, reverse=False, steps=False):
        _sorted_object = self.__sort_it(reverse, steps)
        return list(_sorted_object.values())[-1]


    def evaluate(self, reverse=False, iterations=1):
        if reverse:
            _timing_list = self.__time_eval_desc(iterations)
        else:
            _timing_list = self.__time_eval_asc(iterations)

        _minimum_time = str("{:.10f}s".format(min(_timing_list)))
        _maximum_time = str("{:.10f}s".format(max(_timing_list)))
        _average_time = str("{:.10f}s".format(sum(_timing_list) / iterations))

        eval_dict = {
            "Minimum Time:": _minimum_time,
            "Maximum Time:": _maximum_time,
            "Average Time:": _average_time
        }
        return eval_dict


    def visualize(self, reverse=False, interval=250):
        _vis_list = copy.deepcopy(self.__datalist)

        if not reverse:
            AnimateAlgorithm("Selection Sort", _vis_list, self.__ascending_sort_algo(), interval)
        else:
            AnimateAlgorithm("Selection Sort", _vis_list, self.__descending_sort_algo(), interval)
