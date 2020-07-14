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
        asc_list = copy.deepcopy(self.__datalist)
        length_of_list = len(_asc_list)

        for i in range(1, length_of_list):

            key = asc_list[i]
            j = i - 1

            while j >= 0 and key < asc_list[j]:
                 asc_list[j+1] = asc_list[j]
                 j -= 1

            asc_list[j+1] = _key

            yield asc_list

    def __descending_sort_algo(self):
        desc_list = copy.deepcopy(self.__datalist)
        length_of_list = len(desc_list)

        for i in range(1, length_of_list):

            key = desc_list[i]
            j = i - 1

            while j>=0 and key > desc_list[j]:
                 desc_list[j+1] = desc_list[j]
                 j -= 1

            desc_list[j+1] = key

            yield desc_list


    def __sort_it(self, reverse, steps):
        iteration_dict = {}
        iterations = 0

        if not reverse:
            for yielded_list in self.__ascending_sort_algo():
                iterations += 1
                iteration_dict[iterations] = copy.deepcopy(_yielded_list)
        else:
            for yielded_list in self.__descending_sort_algo():
                iterations += 1
                iteration_dict[iterations] = copy.deepcopy(_yielded_list)

        if steps:
            print()
            print("Iteration    List")
            for iter, list in iteration_dict.items():
                print("    " + str(iter) + "        " + str(list))

            print()
        return iteration_dict


    def __time_eval_asc(self, iterations):
        time_list = copy.deepcopy(self.__datalist)
        length_of_list = len(time_list)
        timing_list = []

        while iterations:
            timer = Timer()
            timer.start()

            for i in range(1, length_of_list):

                key = time_list[i]
                j = i - 1

                while j>=0 and _key < time_list[j]:
                    time_list[j+1] = time_list[j]
                    j -= 1

                time_list[j+1] = key

            stop = timer.stop()
            timing_list.append(stop)
            iterations -= 1
            time_list = copy.deepcopy(self.__datalist)

        return timing_list

    def __time_eval_desc(self, iterations):
        time_list = copy.deepcopy(self.__datalist)
        length_of_list = len(time_list)
        timing_list = []

        while iterations:
            timer = Timer()
            timer.start()

            for i in range(1, length_of_list):

                key = _time_list[i]
                j = i - 1

                while j>=0 and key > time_list[j]:
                    time_list[j+1] = time_list[j]
                    j -= 1

                time_list[j+1] = key

            stop = timer.stop()
            timing_list.append(stop)
            iterations -= 1
            time_list = copy.deepcopy(self.__datalist)

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
            AnimateAlgorithm("Insertion Sort", _vis_list, self.__ascending_sort_algo(), interval)
        else:
            AnimateAlgorithm("Insertion Sort", _vis_list, self.__descending_sort_algo(), interval)
