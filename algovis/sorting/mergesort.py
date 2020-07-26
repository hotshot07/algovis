"""Merge sort module in sorting package.

The module is used to demonstrate the working of merge sort algorithm

Exported methods from MergeSort class:
    sort
    evaluate
    visualize
    info
    code

Helper methods:
    __sort_it
    __eval_helper
    __fast_merge_asc
    __fast_merge_desc
    __no_len_ms


Helper generators:
    __ascending_sort_merge_algo
    __descending_sort_merge_algo
    __merge_algo
    __animate_sort_it

Example usage:
    bs_object = sorting.MergeSort(datalist)
    bs_object.sort(reverse = True, steps = True)
"""

import copy

from ._base_sorting import BaseClass
from ._timer import Timer
from ._animation import animate_algorithm


class MergeSort(BaseClass):
    """Merge Sort class which contains methods for analyzing merge sort algorithm.

    Attributes:
        _datalist (list): List of ints provided by the user
    """

    def __init__(self, datalist):
        """Initializes Merge Sort class with datalist.

        Args:
            datalist (list): The list provided by the user
        """
        super().__init__(datalist)
        self._datalist = datalist

    def __repr__(self):
        """__repr__ for MergeSort class"""
        return f'algovis.sorting.mergesort.MergeSort({self._datalist})'

    def __ascending_sort_merge_algo(self, passed_list, start, mid, end):
        """Helper generator for the ascending merge sort algorithm.

        It is called by __merge_algo

        Yields:
              asc_list (list): yields list after each pass of merge sort on
                               the list

        """
        merged = []
        leftIdx = start
        rightIdx = mid + 1

        while leftIdx <= mid and rightIdx <= end:
            if passed_list[leftIdx] < passed_list[rightIdx]:
                merged.append(passed_list[leftIdx])
                leftIdx += 1
            else:
                merged.append(passed_list[rightIdx])
                rightIdx += 1

        while leftIdx <= mid:
            merged.append(passed_list[leftIdx])
            leftIdx += 1

        while rightIdx <= end:
            merged.append(passed_list[rightIdx])
            rightIdx += 1

        for i, sorted_val in enumerate(merged):
            passed_list[start + i] = sorted_val

        yield passed_list

    def __descending_sort_merge_algo(self, passed_list, start, mid, end):
        """Helper generator for the descending merge sort algorithm.

        It is called by __merge_algo

        Yields:
              desc_list (list): yields list after each pass of merge sort on
                               the list

        """
        merged = []
        leftIdx = start
        rightIdx = mid + 1

        while leftIdx <= mid and rightIdx <= end:
            if passed_list[leftIdx] > passed_list[rightIdx]:
                merged.append(passed_list[leftIdx])
                leftIdx += 1
            else:
                merged.append(passed_list[rightIdx])
                rightIdx += 1

        while leftIdx <= mid:
            merged.append(passed_list[leftIdx])
            leftIdx += 1

        while rightIdx <= end:
            merged.append(passed_list[rightIdx])
            rightIdx += 1

        for i, sorted_val in enumerate(merged):
            passed_list[start + i] = sorted_val

        yield passed_list

    def __merge_algo(self, passed_list, start, end, reverse):
        """Helper method for merge sort

        It calls the __ascend... or __descen... recursively to perform
        merge sort algo on the list.

        Yields:
            passed_list (list): list on which we're performing the algo is
                                yielded after each iteration
        """
        if end <= start:
            return

        mid = start + ((end - start + 1) // 2) - 1
        yield from self.__merge_algo(passed_list, start, mid, reverse)
        yield from self.__merge_algo(passed_list, mid + 1, end, reverse)
        if not reverse:
            yield from self.__ascending_sort_merge_algo(passed_list, start, mid, end)
        else:
            yield from self.__descending_sort_merge_algo(passed_list, start, mid, end)
        yield passed_list

    def __animate_sort_it(self, reverse=False):
        """The generator passed to _animate_algorithm.

        Args:
            reverse (bool): Boolean to sort list in reverse

        Yields:
            iter_list (list): List after each iteration of Merge sort
        """
        passed_list = copy.deepcopy(self._datalist)
        for iter_list in self.__merge_algo(passed_list, 0, len(passed_list) - 1, reverse):
            yield iter_list

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
        passed_list = copy.deepcopy(self._datalist)
        iteration_dict = {}
        iterations = 0

        # the 0th iteration is basically the passed list
        iteration_dict[iterations] = self._datalist

        for yielded_list in self.__merge_algo(passed_list, 0, len(passed_list) - 1, reverse):
            iterations += 1
            iteration_dict[iterations] = copy.deepcopy(yielded_list)

        if steps:
            super()._print_steps(iteration_dict, "Merge Sort")

        return iteration_dict

    def __fast_merge_asc(self, array1, array2):
        """Helper method for 'evaluate'

        using https://stackoverflow.com/questions/7063697/why-is-my-mergesort-so-slow-in-python
        Merge Sort with optimizations for making it much faster

        """
        merged_array = []
        while array1 or array2:
            if not array1:
                merged_array.append(array2.pop())
            elif (not array2) or array1[-1] > array2[-1]:
                merged_array.append(array1.pop())
            else:
                merged_array.append(array2.pop())
        merged_array.reverse()
        return merged_array

    def __fast_merge_desc(self, array1, array2):
        """Helper method for 'evaluate'.

        Similar to above method, in descending order

        """
        merged_array = []
        while array1 or array2:
            if not array1:
                merged_array.append(array2.pop())
            elif (not array2) or array1[-1] < array2[-1]:
                merged_array.append(array1.pop())
            else:
                merged_array.append(array2.pop())
        merged_array.reverse()
        return merged_array

    def __no_len_ms(self, array, reverse):
        """Helper method for 'evaluate'.

        It calls __fast-merge which is optimized version of mergesort for evaluation

        Returns:
            A sorted array, which is not used anywhere
        """
        n = len(array)
        if n <= 1:
            return array
        mid = int(n / 2)
        left = array[:mid]
        right = array[mid:]
        if not reverse:
            return self.__fast_merge_asc(self.__no_len_ms(left, reverse), self.__no_len_ms(right, reverse))
        return self.__fast_merge_desc(self.__no_len_ms(left, reverse), self.__no_len_ms(right, reverse))

    def __eval_helper(self, reverse, iterations):
        """Helper method for 'evaluate' method

        Evaluating time of ascending merge sort algorithm.Takes in the
        'iterations' provided by the user and performs sorting that many times.

        Args:
            iterations (int): Number of times to perform sorting on this algo
            reverse (bool): check if user wants to reverse the list

        Returns:
            timing_list (list): A list of time taken for fully sorting the
                                list 'iterations' number of times
        """
        timing_list = []

        while iterations:
            time_list = copy.deepcopy(self._datalist)

            timer = Timer()
            timer.start()

            self.__no_len_ms(time_list, reverse)

            stop = timer.stop()
            timing_list.append(stop)

            iterations -= 1

        return timing_list

    def sort(self, reverse=False, steps=False):
        """Performs merge sort on the list provided by the user.

        Args:
            reverse (bool): Optional; (default: False)
                            If True, sorts the list in descending order
            steps (bool): Optional; (default: False)
                            If set to True, shows iteration of each pass of
                            mergesort on the list

        Returns:
            sorted_list (list): sorted list
        """
        _sorted_object = self.__sort_it(reverse, steps)

        sorted_list = list(_sorted_object.values())[-1]

        return sorted_list

    def evaluate(self, reverse=False, iterations=1):
        """Prints the time taken to perform merge sort in nanoseconds and
        seconds to the console.

        Set optional parameter 'iterations' to the number of times you want to
        perform merge sort on the list. After every iteration, the list is reset to
        it's original unsorted state.

        Set optional parameter 'reverse' to True to sort the list in descending order.

        Args:
            reverse (bool): Optional; (default: False)
                            If True, sorts the list in descending order
            iterations (int): Optional; (default: 1)
                              Number of times to perform merge sort on list

        Raises:
            TypeError: When user inputs anything other than an int for iteration
        """

        if not isinstance(iterations, int):
            raise TypeError('Iterations can only be int datatype')

        _timing_list = self.__eval_helper(reverse, iterations)

        _minimum_time = min(_timing_list)
        _maximum_time = max(_timing_list)
        _average_time = int(sum(_timing_list) / iterations)

        _eval_dict = {
            "Minimum Time": _minimum_time,
            "Maximum Time": _maximum_time,
            "Average Time": _average_time
        }

        return super()._print_evaluate(_eval_dict, "Merge Sort")

    def visualize(self, reverse=False, interval=250):
        """Shows a visualization using matplotlib of merge sort performed on
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

        animate_algorithm("Merge Sort", _vis_list, self.__animate_sort_it(reverse), interval, operations=True)

    @classmethod
    def info(cls):
        """Class method that provides information on merge sort."""
        path_to_information = "algovis/sorting/_markdown_files/mergesort.md"
        return super()._print_info(path_to_information)

    @classmethod
    def code(cls):
        """Class method that prints code to the console."""
        my_code = """
        def merge(array, left_index, right_index, middle):
            # Make copies of both arrays we're trying to merge

            # The second parameter is non-inclusive, so we have to increase by 1
            left_copy = array[left_index:middle + 1]
            right_copy = array[middle+1:right_index+1]

            # Initial values for variables that we use to keep
            # track of where we are in each array
            left_copy_index = 0
            right_copy_index = 0
            sorted_index = left_index

            # Go through both copies until we run out of elements in one
            while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

                # If our left_copy has the smaller element, put it in the sorted
                # part and then move forward in left_copy (by increasing the pointer)
                if left_copy[left_copy_index] <= right_copy[right_copy_index]:
                    array[sorted_index] = left_copy[left_copy_index]
                    left_copy_index = left_copy_index + 1
                # Opposite from above
                else:
                    array[sorted_index] = right_copy[right_copy_index]
                    right_copy_index = right_copy_index + 1

                # Regardless of where we got our element from
                # move forward in the sorted part
                sorted_index = sorted_index + 1

            # We ran out of elements either in left_copy or right_copy
            # so we will go through the remaining elements and add them
            while left_copy_index < len(left_copy):
                array[sorted_index] = left_copy[left_copy_index]
                left_copy_index = left_copy_index + 1
                sorted_index = sorted_index + 1

            while right_copy_index < len(right_copy):
                array[sorted_index] = right_copy[right_copy_index]
                right_copy_index = right_copy_index + 1
                sorted_index = sorted_index + 1

        def merge_sort(array, left_index, right_index):
            if left_index >= right_index:
                return

            middle = (left_index + right_index)//2
            merge_sort(array, left_index, middle)
            merge_sort(array, middle + 1, right_index)
            merge(array, left_index, right_index, middle)

        #from https://stackabuse.com/merge-sort-in-python/
        """
        return super()._print_code(my_code)
