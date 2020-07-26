"""Insertion sort module in sorting package.

The module is used to demonstrate the working of insertion sort algorithm

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
    bs_object = sorting.InsertionSort(datalist)
    bs_object.evaluate(iterations = 20, reverse = True)
"""
import copy

from ._base_sorting import BaseClass
from ._timer import Timer
from ._animation import animate_algorithm


class InsertionSort(BaseClass):
    """InsertionSort class which contains methods for analyzing insertion sort algorithm.

    Attributes:
        _datalist (list): List of ints provided by the user
    """

    def __init__(self, datalist):
        """Initializes Insertion Sort class with datalist.

        Args:
            datalist (list): The list provided by the user
        """
        super().__init__(datalist)
        self._datalist = datalist

    def __repr__(self):
        """__repr__ for InsertionSort class"""
        return f'algovis.sorting.insertionsort.InsertionSort({self._datalist})'

    def __ascending_sort_algo(self):
        """Helper generator for the ascending insertion sort algorithm.

        It yields list after every iteration of insertion sort till the
        list is sorted

        Yields:
              asc_list (list): yields complete list after each iteration of
                               the algorithm

        """
        asc_list = copy.deepcopy(self._datalist)
        length_of_list = len(asc_list)

        for i in range(1, length_of_list):

            key = asc_list[i]
            j = i - 1

            while j >= 0 and key < asc_list[j]:
                asc_list[j + 1] = asc_list[j]
                j -= 1

            asc_list[j + 1] = key

            yield asc_list

    def __descending_sort_algo(self):
        """Helper generator for the descending insertion sort algorithm.

        It yields list after every iteration of insertion sort till the
        list is sorted

        Yields:
              asc_list (list): yields complete list after each iteration of
                               the algorithm

        """
        desc_list = copy.deepcopy(self._datalist)
        length_of_list = len(desc_list)

        for i in range(1, length_of_list):

            key = desc_list[i]
            j = i - 1

            while j >= 0 and key > desc_list[j]:
                desc_list[j + 1] = desc_list[j]
                j -= 1

            desc_list[j + 1] = key

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
            super()._print_steps(iteration_dict, "Insertion Sort")

        return iteration_dict

    def __time_eval_asc(self, iterations):
        """Helper method for 'evaluate' method

        Evaluating time of ascending insertion sort algorithm.Takes in the
        'iterations' provided by the user and performs sorting that many times.

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

            for i in range(1, length_of_list):

                key = time_list[i]
                j = i - 1

                while j >= 0 and key < time_list[j]:
                    time_list[j + 1] = time_list[j]
                    j -= 1

                time_list[j + 1] = key

            stop = timer.stop()
            timing_list.append(stop)
            iterations -= 1
            time_list = copy.deepcopy(self._datalist)

        return timing_list

    def __time_eval_desc(self, iterations):
        """Helper method for 'evaluate' method

        Evaluating time of descending insertion sort algorithm. Works in similar way
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
            timer = Timer()
            timer.start()

            for i in range(1, length_of_list):

                key = time_list[i]
                j = i - 1

                while j >= 0 and key > time_list[j]:
                    time_list[j + 1] = time_list[j]
                    j -= 1

                time_list[j + 1] = key

            stop = timer.stop()
            timing_list.append(stop)
            iterations -= 1
            time_list = copy.deepcopy(self._datalist)

        return timing_list

    def sort(self, reverse=False, steps=False):
        """Performs insertion sort on the list provided by the user.

        Args:
            reverse (bool): Optional; (default: False)
                            If True, sorts the list in descending order
            steps (bool): Optional; (default: False)
                            If set to True, shows iteration of each pass of
                            insertion on the list

        Returns:
            sorted_list (list): sorted list
        """
        _sorted_object = self.__sort_it(reverse, steps)

        sorted_list = list(_sorted_object.values())[-1]

        return sorted_list

    def evaluate(self, reverse=False, iterations=1):
        """Prints the time taken to perform insertion sort in nanoseconds and
        seconds to the console.

        Set optional parameter 'iterations' to the number of times you want to
        perform insertion sort on the list. After every iteration, the list is reset to
        it's original unsorted state.

        Set optional parameter 'reverse' to True to sort the list in descending order.

        Args:
            reverse (bool): Optional; (default: False)
                            If True, sorts the list in descending order
            iterations (int): Optional; (default: 1)
                              Number of times to perform insertion sort on list

        Raises:
            TypeError: When user inputs anything other than an int for iteration
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

        return super()._print_evaluate(_eval_dict, "Insertion Sort")

    def visualize(self, reverse=False, interval=250):
        """Shows a visualization using matplotlib of insertion sort performed on
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
            animate_algorithm("Insertion Sort", _vis_list, self.__ascending_sort_algo(), interval)
        else:
            animate_algorithm("Insertion Sort", _vis_list, self.__descending_sort_algo(), interval)

    @classmethod
    def info(cls):
        """Class method that provides information on insertion sort."""
        path_to_information = "algovis/sorting/_markdown_files/insertionsort.md"
        return super()._print_info(path_to_information)

    @classmethod
    def code(cls):
        """Class method that prints the function for insertion sort in console."""
        my_code = """
        def insertion_sort(array):

            # Traverse through 1 to len(array)
            for i in range(1, len(array)):

                key = arr[i]

                # Move elements of arr[0..i-1], that are
                # greater than key, to one position ahead
                # of their current position
                j = i-1
                while j >= 0 and key < array[j] :
                        array[j + 1] = array[j]
                        j -= 1
                array[j + 1] = key
        """
        return super()._print_code(my_code)
