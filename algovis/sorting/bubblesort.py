"""Bubble sort module in sorting package.

The module is used to demonstrate the working of bubble sort algorithm

Exported methods:
    sort
    evaluate
    visualize
    info
    code

Helper methods:
    __sort_it
    __time_eval_asc
    __time_eval_desc

Helper generators:
    __ascending_sort_algo
    __descending_sort_algo

Example usage:
    bs_object = sorting.BubbleSort(datalist)
    bs_object.sort(reverse = True, steps = True)
"""
import copy
import os
import sys

from ._base_sorting import BaseClass
from ._timer import Timer
from ._animation import animate_algorithm


class BubbleSort(BaseClass):
    """Bubble Sort class which contains methods for analyzing bubble sort algorithm.

    Attributes:
        _datalist (list): List of ints provided by the user
    """

    def __init__(self, datalist):
        """Initializes Bubble Sort class with datalist.

        Args:
            datalist (list): The list provided by the user
        """
        super().__init__(datalist)
        self._datalist = datalist

    def __repr__(self):
        """__repr__ for BubbleSort class"""
        return f'algovis.sorting.bubblesort.BubbleSort({self._datalist})'

    def __ascending_sort_algo(self):
        """Helper generator for the ascending bubble sort algorithm.

        It yields list after every iteration of bubble sort till the
        list is sorted

        Yields:
              asc_list (list): yields list after each pass of bubble sort on
                               the list

        """
        asc_list = copy.deepcopy(self._datalist)
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

    def __descending_sort_algo(self):
        """Helper generator for the descending bubble sort algorithm.

        It yields list after every iteration of bubble sort till the
        list is sorted

        Yields:
              desc_list (list): yields list after each pass of bubble sort on
                               the list

        """
        desc_list = copy.deepcopy(self._datalist)
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

    def __sort_it(self, reverse, steps):
        """Helper method for 'sort' method

        It checks which generator to call based on reverse. Then it stores every
        iteration of yielded list in a dictionary. If steps is true, then _print_steps
        is called from BaseClass and the dictionary iteration_dict is passed to it which
        prints the steps

        Args:
            reverse (bool): based on reverse, we call the generator to either sort the list
                            in ascending or descending order
            steps (bool): If true, it calls function to print steps

        Returns:
            iteration_dict (dict):
        """
        iteration_dict = {}
        iterations = 0

        # the 0th iteration is basically the passed list
        iteration_dict[iterations] = self._datalist

        if not reverse:
            for yielded_list in self.__ascending_sort_algo():
                iterations += 1
                iteration_dict[iterations] = copy.deepcopy(yielded_list)
        else:
            for yielded_list in self.__descending_sort_algo():
                iterations += 1
                iteration_dict[iterations] = copy.deepcopy(yielded_list)

        if steps:
            super()._print_steps(iteration_dict, "Bubble Sort")

        return iteration_dict

    # Tested code
    # my_list = [random.randint(0, 1000) for i in range(100)]
    # bs = sorting.BubbleSort(my_list)
    # bs.evaluate(iterations=1000)

    # average time for this method on my mac 683527ns
    # average time using generators is 821957ns
    # as this algo scales exponentially, I didn't call the generators

    def __time_eval_asc(self, iterations):
        """Helper method for 'evaluate' method

        Evaluating time of ascending bubble sort algorithm. Didn't use
        generators as function overheads caused increase in time of execution and
        this algo scales exponentially. Takes in the 'iterations' provided by
        the user and performs sorting that many times.

        Args:
            iterations (int): Number of times to perform sorting on this algo

        Returns:
            timing_list (list): A list of time taken for fully sorting the list
        """
        time_list = copy.deepcopy(self._datalist)
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
            time_list = copy.deepcopy(self._datalist)

        return timing_list

    def __time_eval_desc(self, iterations):
        """Helper method for 'evaluate' method

        Evaluating time of descending bubble sort algorithm. Works in similar way
        to __time_eval_asc

        Args:
            iterations (int): Number of times to perform sorting on this algo

        Returns:
            timing_list (list): A list of time taken for fully sorting the list
        """
        time_list = copy.deepcopy(self._datalist)
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
            time_list = copy.deepcopy(self._datalist)

        return timing_list

    def sort(self, reverse=False, steps=False):
        """Performs optimized bubble sort on the list provided by the user.

        Args:
            reverse (bool): Optional; (default: False)
                            If True, sorts the list in descending order
            steps (bool): Optional; (default: False)
                            If set to True, shows iteration of each pass of
                            bubblesort on the list

        Returns:
            sorted_list (list): sorted list
        """
        _sorted_object = self.__sort_it(reverse, steps)

        # sorted object is a dict so we convert it into a list
        # and return the last element which is the sorted list
        sorted_list = list(_sorted_object.values())[-1]

        return sorted_list

    def evaluate(self, reverse=False, iterations=1):
        """Prints the time taken to perform optimized bubble sort in nanoseconds and
        seconds to the console.

        Set optional parameter 'iterations' to the number of times you want to
        perform bubble sort on the list. After every iteration, the list is reset to
        it's original unsorted state.

        Set optional parameter 'reverse' to True to sort the list in descending order.

        Args:
            reverse (bool): Optional; (default: False)
                            If True, sorts the list in descending order
            iterations (int): Optional; (default: 1)
                              Number of times to perform bubble sort on list

        Raises:
            TypeError: When user inputs anything other than an int for number
                       or iteration
        """
        if not isinstance(iterations, int):
            raise TypeError('Iterations can only be int datatype')

        if reverse:
            _timing_list = self.__time_eval_desc(iterations)
        else:
            _timing_list = self.__time_eval_asc(iterations)

        _minimum_time = min(_timing_list)
        _maximum_time = max(_timing_list)
        _average_time = int(sum(_timing_list) / iterations)

        _eval_dict = {
            "Minimum Time": _minimum_time,
            "Maximum Time": _maximum_time,
            "Average Time": _average_time
        }

        return super()._print_evaluate(_eval_dict, "Bubble Sort")

    def visualize(self, reverse=False, interval=250):
        """Shows a visualization using matplotlib of bubble sort performed on
        the list user passed.

        Set optional parameter 'interval' to change the delay between frames
        in milliseconds.

        Args:
            reverse (bool): Optional; (default: False)
                            If True, sorts the list in descending order
            interval (int): Optional; (default: 250)
                            Delay between frames in milliseconds

        Raises:
            TypeError: An error when user inputs anything other than int for
                       interval
        """

        if not isinstance(interval, int):
            raise TypeError('Interval can only be int datatype')

        _vis_list = copy.deepcopy(self._datalist)

        if not reverse:
            animate_algorithm("Bubble Sort", _vis_list, self.__ascending_sort_algo(), interval)
        else:
            animate_algorithm("Bubble Sort", _vis_list, self.__descending_sort_algo(), interval)

    @classmethod
    def info(cls):
        """Class method that provides information on bubble sort."""
        dir = os.path.dirname(__file__)
        path_to_information = os.path.join(dir, '_markdown_files', 'bubblesort.md')
        return super()._print_info(path_to_information)

    @classmethod
    def code(cls):
        """Class method that prints the function for bubble sort in console."""
        my_code = """
        # Optimized bubble sort
        def bubble_sort(array):

            length_of_list = len(array)

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
