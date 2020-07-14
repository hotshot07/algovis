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
        return f'algovis.sorting.selectionsort.SelectionSort({self.__datalist})'

    def __ascending_sort_algo(self):
        asc_list = copy.deepcopy(self.__datalist)
        length_of_list = len(asc_list)

        for i in range(length_of_list):
            #minimum unsorted value
            min_val = asc_list[i]
            min_idx = i
            for j in range(i, length_of_list):
                if asc_list[j] < min_val:
                    min_val = asc_list[j]
                    min_idx = j

            asc_list[i], asc_list[_min_idx]  = asc_list[_min_idx], asc_list[i]
            yield asc_list

    def __descending_sort_algo(self):
        asc_list = copy.deepcopy(self.__datalist)
        length_of_list = len(asc_list)

        for i in range(length_of_list):
            #minimum unsorted value
            max_val = asc_list[i]
            max_idx = i
            for j in range(i, length_of_list):
                if asc_list[j] > max_val:
                    max_val = asc_list[j]
                    max_idx = j

            asc_list[i], asc_list[_max_idx]  = asc_list[_max_idx], asc_list[i]
            yield asc_list

    def __sort_it(self, reverse, steps):
            iteration_dict = {}
            iterations = 0

            if not reverse:
                for yielded_list in self.__ascending_sort_algo():
                    iterations += 1
                    iteration_dict[iterations] = copy.deepcopy(yielded_list)
            else:
                for yielded_list in self.__descending_sort_algo():
                    iterations += 1
                    iteration_dict[iterations] = copy.deepcopy(yielded_list)

            if steps:
                print()
                print("Iteration    List")
                for iter, list in iteration_dict.items():
                    print("    " + str(_iter) + "        " + str(_list))

                print()
            return iteration_dict


    def __time_eval_asc(self, iterations):
        time_list = copy.deepcopy(self.__datalist)
        length_of_list = len(time_list)
        timing_list = []

        while iterations:

            timer = Timer()
            timer.start()

            for i in range(length_of_list):
                #minimum unsorted value
                min_val = time_list[i]
                min_idx = i
                for j in range(i, length_of_list):
                    if time_list[j] < min_val:
                        min_val = time_list[j]
                        min_idx = j

                time_list[i], time_list[_min_idx]  = time_list[_min_idx], time_list[i]

            stop = timer.stop()
            timing_list.append(stop)
            iterations -= 1
            time_list = copy.deepcopy(self.__datalist)

        return timing_list



    def __time_eval_desc(self, iterations):
        time_list = copy.deepcopy(self.__datalist)
        length_of_list = len(_time_list)
        timing_list = []

        while iterations:

            timer = Timer()
            timer.start()

            for i in range(_length_of_list):
                #minimum unsorted value
                max_val = time_list[i]
                max_idx = i
                for j in range(i, length_of_list):
                    if time_list[j] > max_val:
                        max_val = time_list[j]
                        max_idx = j

                time_list[i], time_list[_max_idx]  = time_list[_max_idx], time_list[i]

            stop = timer.stop()
            timing_list.append(stop)
            iterations -= 1
            time_list = copy.deepcopy(self.__datalist)

        return timing_list



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
