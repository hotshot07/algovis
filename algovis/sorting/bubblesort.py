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

        iteration_dict[iterations] = self.__datalist

        if not reverse:
            for yielded_list in self.__ascending_sort_algo():
                iterations += 1
                iteration_dict[iterations] = copy.deepcopy(yielded_list)
        else:
            for yielded_list in self.__descending_sort_algo():
                iterations += 1
                iteration_dict[iterations] = copy.deepcopy(yielded_list)

        if steps:
            super()._print_steps(iteration_dict)

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

                for i in range(length_of_list - number_of_iterations - 1):
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

        _minimum_time = min(_timing_list)
        _maximum_time = max(_timing_list)
        _average_time = int(sum(_timing_list) / iterations)

        eval_dict = {
            "Minimum Time": _minimum_time,
            "Maximum Time": _maximum_time,
            "Average Time": _average_time
        }

        return super()._print_evaluate(eval_dict)

    def visualize(self, reverse=False, interval=250):
        _vis_list = copy.deepcopy(self.__datalist)

        if not reverse:
            AnimateAlgorithm("Bubble Sort", _vis_list, self.__ascending_sort_algo(), interval)
        else:
            AnimateAlgorithm("Bubble Sort", _vis_list, self.__descending_sort_algo(), interval)

    @classmethod
    def info(cls):
        path_to_information = "algovis/sorting/_markdown_files/bubblesort.md"
        return super()._print_info(path_to_information)

    @classmethod
    def code(cls):
        my_code = """
        def bubbleSort(arr):

            length_of_list = len(arr) 
           
            # Traverse through all array elements 
            for i in range(length_of_list): 
                swapped = False
          
                # Last i elements are already in place 
                for j in range(0, length_of_list- i -1): 
           
                    # traverse the array from 0 to 
                    # length_of_list-i-1. Swap if the element  
                    # found is greater than the 
                    # next element 
                    if arr[j] > arr[j+1] : 
                        arr[j], arr[j+1] = arr[j+1], arr[j] 
                        swapped = True
          
                # If no two elements were swapped 
                # by inner loop, then break 
                if swapped == False: 
                    break

            return arr
        """

        return super()._print_code(my_code)
