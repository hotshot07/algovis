"""
Author: Mayank Arora (hotshot07)
"""
from ._base_class import BaseClass
from ._timer import Timer
from ._animation import AnimateAlgorithm
import copy


class BubbleSort(BaseClass):

    def __init__(self, datalist):
        super().__init__(datalist)
        self.__datalist = datalist

    def __repr__(self):
        return f'algovis.sorting.bubblesort.BubbleSort({self.__datalist})'

    # A generator for the ascending bubble sort algorithm
    def __ascending_sort_algo(self):
        asc_list = copy.deepcopy(self.__datalist)
        length_of_list = len(asc_list)
        has_swapped = True
        number_of_iterations = 0

        while has_swapped:
            has_swapped = False

            for i in range(length_of_list - number_of_iterations - 1):
                if asc_list[i] > asc_list[i + 1]:
                    asc_list[i], asc_list[i + 1] = asc_list[i + 1], asc_list[i]
                    has_swapped = True

            number_of_iterations += 1
            yield asc_list

    # A generator for the descending bubble sort algorithm
    def __descending_sort_algo(self):
        desc_list = copy.deepcopy(self.__datalist)
        length_of_list = len(desc_list)
        has_swapped = True
        number_of_iterations = 0

        while has_swapped:
            has_swapped = False

            for i in range(length_of_list - number_of_iterations - 1):
                if desc_list[i] < desc_list[i + 1]:
                    desc_list[i], desc_list[i + 1] = desc_list[i + 1], desc_list[i]

                    has_swapped = True

            number_of_iterations += 1
            yield desc_list

    # The function that is called by sort method
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
            # print()
            # print("Iteration    List")
            # for iter, list in iteration_dict.items():
            #     print("    " + str(iter) + "        " + str(list))

            # print()
            super()._print_evaluate(iteration_dict)
        return iteration_dict

    # Evaluating time of ascending bubble sort
    # Didn't use generators as I dont want to waste time in
    # function overheads
    def __time_eval_asc(self, iterations):
        time_list = copy.deepcopy(self.__datalist)
        length_of_list = len(time_list)
        timing_list = []

        while iterations:
            timer = Timer()
            timer.start()
            has_swapped = True
            number_of_iterations = 0

            while has_swapped:
                has_swapped = False

                for i in range(length_of_list - number_of_iterations - 1):
                    if time_list[i] > time_list[i + 1]:
                        time_list[i], time_list[i + 1] = time_list[i + 1], time_list[i]

                        has_swapped = True

                number_of_iterations += 1

            stop = timer.stop()
            timing_list.append(stop)
            iterations -= 1
            time_list = copy.deepcopy(self.__datalist)

        return timing_list

    # Evaluating time of descending bubble sort
    def __time_eval_desc(self, iterations):
        time_list = copy.deepcopy(self.__datalist)
        length_of_list = len(time_list)
        timing_list = []

        while iterations:
            has_swapped = True
            number_of_iterations = 0

            timer = Timer()
            timer.start()

            while has_swapped:
                has_swapped = False

                for i in range(_length_of_list - _number_of_iterations - 1):
                    if time_list[i] < time_list[i + 1]:
                        time_list[i], time_list[i + 1] = time_list[i + 1], time_list[i]

                        has_swapped = True

                number_of_iterations += 1

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
            AnimateAlgorithm("Bubble Sort", _vis_list, self.__ascending_sort_algo(), interval)
        else:
            AnimateAlgorithm("Bubble Sort", _vis_list, self.__descending_sort_algo(), interval)

    @classmethod
    def info(cls):
        information = """
           Bubble Sort

In Bubble Sort  we look at pairs of adjacent elements in an array,
one pair at a time, and swap their positions if the first element is
larger than the second, or simply move on if it isn't.

        ---Time Complexity---
        "Worse case: O(n^2)
        "Average case: O(n^2)
        "Best case: O(n)

        ---Space Complexity---
        O(n) total, O(1) auxiliary

        ---Algorithm---
        procedure bubbleSort(A : list of sortable items)
            n := length(A)
            repeat
                swapped := false
                    for i := 1 to n - 1 inclusive do
                        if A[i - 1] > A[i] then
                        swap(A[i - 1], A[i])
                        swapped = true
                        end if
                    end for
                    n := n - 1
                until not swapped
        end procedure"""

        return information
