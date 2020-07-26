"""Quick sort module in sorting package.

The module is used to demonstrate the working of quick sort algorithm. This module
is significantly differently designed than other sorting modules currently in package,
trading readibility for complexity, although the API is same.

Exported methods from QuickSort class:
    sort
    evaluate
    visualize
    info
    code

Helper methods:
    __choose_pivot
    __sort_it
    __print_steps_quick
    __eval_helper


Helper generators:
    __quicksort

Example usage:
    qs_object = sorting.QuickSort(datalist)
    qs_object.sort(pivot = "random", reverse = True, steps = True)
"""

import copy
import random

from rich.console import Console
from rich.table import Table

from ._base_sorting import BaseClass
from ._timer import Timer
from ._animation import animate_algorithm


class QuickSort(BaseClass):
    """Quick Sort class which contains methods for analyzing quick sort algorithm.

    Attributes:
        _datalist (list): List of ints provided by the user
    """

    def __init__(self, datalist):
        """Initializes Quick Sort class with datalist.

        Args:
            datalist (list): The list provided by the user
        """
        super().__init__(datalist)
        self._datalist = datalist

    def __repr__(self):
        """__repr__ for QuickSort class"""
        return f'algovis.sorting.quicksort.QuickSort({self._datalist})'

    # The next two functions are based on Lomuto partition sceheme quicksort
    # inspired by
    # https://www.geeksforgeeks.org/quicksort-using-random-pivoting/

    def __choose_pivot(self, arr, start, end, choice):
        """Helper method called by __quicksort to choose a pivot

        It chooses a pivot based on user input and what is basically does
        is that it swaps the 'pivot' with the first element and returns the
        modded array

        Args:
            arr (list): The list passed by __quicksort
            start (int): Index of first element of the array
            end (int): Index of last element of the array
            choice (str): User input
        """
        if choice == 'first':
            return arr
        elif choice == 'last':
            arr[start], arr[end] = arr[end], arr[start]
            return arr
        elif choice == 'random':
            randpivot = random.randrange(start, end)
            arr[start], arr[randpivot] = arr[randpivot], arr[start]
            return arr
        elif choice == 'middle':
            middle_pivot = start + (end - start) // 2
            arr[start], arr[middle_pivot] = arr[middle_pivot], arr[start]
            return arr
        else:
            return arr

    def __quicksort(self, arr, start, stop, choice, reverse, vis=False):
        """The helper generator called by __sort_it

        Args:
            arr (list): The list passed by __quicksort
            start (int): Index of first element of the array
            stop (int): Index of last element of the array
            choice (str): User input
            reverse (bool): If true, sorts the list in descending order
            vis (bool): Set to true for animate_algorithm, yields array at
                        different places throughout the generator

        Yields:
            arr (list): If vis == True, it yields strategically placed arrays
                        throughout the generator

            elem_pivot, arr[start:stop + 1], arr (int, list, list):
                        Yields a tuple of pivot element, list modified and total list
                        which help make the print steps

        """
        if start < stop:
            arr = self.__choose_pivot(arr, start, stop, choice)
            pivot = start
            elem_pivot = arr[pivot]  # pivot
            i = start + 1

            if vis:
                yield arr
            # a variable to memorize where the
            # partition in the array starts from.
            for j in range(start + 1, stop + 1):

                # if not reverse and the current element is smaller or equal to pivot,
                # shift it to the left side of the partition else vice versa

                if reverse:
                    if arr[j] >= arr[pivot]:
                        arr[i], arr[j] = arr[j], arr[i]
                        if vis:
                            yield arr
                        i = i + 1
                else:
                    if arr[j] <= arr[pivot]:
                        arr[i], arr[j] = arr[j], arr[i]
                        if vis:
                            yield arr
                        i = i + 1

            arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
            pivot = i - 1

            if vis:
                yield arr
            else:
                yield elem_pivot, arr[start:stop + 1], arr
            yield from self.__quicksort(arr, start, pivot - 1, choice, reverse, vis)
            yield from self.__quicksort(arr, pivot + 1, stop, choice, reverse, vis)

    # OPTIMIZE IT by using a dictionary in next patch
    def __sort_it(self, reverse, steps, pivot, eval_=False):
        """ Function called by both, __eval_helper and __sort_it

        If the function is used for evaluation, then it just calls __quicksort
        and does nothing with returned tuple, waits for calls to finish and then
        returns None.

        If the function is called by __sort_it, then it creates a list of lists of
        every iteration and stores the data in it. If the steps == True, it calls
        __print_steps to display the evaluation on the terminal. It returns the
        iteration_list.

        Args:
        reverse (bool): bool passed to __quicksort
        steps (bool): print steps if it's true
        pivot (str): pivot chosen by the user
        eval (bool): (default: False)
        """
        if not eval_:
            passed_list = copy.deepcopy(self._datalist)

            iteration_list = []
            iterations = 0
            zeroth_iter = " ".join(str(x) for x in passed_list)
            iteration_list.append([str(0), str(" "), zeroth_iter, zeroth_iter])

            for elem_pivot, array_in_cons, array in self.__quicksort(passed_list, 0, len(passed_list) - 1, pivot, reverse):
                temp_list = []
                iterations += 1
                temp_list.append(str(iterations))
                temp_list.append(str(elem_pivot))
                temp_list.append(" ".join(str(x) for x in array_in_cons))
                temp_list.append(" ".join(str(x) for x in array))
                iteration_list.append(temp_list)

            if steps:
                self.__print_steps_quick(iteration_list)

            return iteration_list
        else:
            passed_list = copy.deepcopy(self._datalist)

            for elem_pivot, array_in_cons, array in self.__quicksort(passed_list, 0, len(passed_list) - 1, pivot, reverse):
                pass

            return

    def __print_steps_quick(self, list_of_iterations):
        """Helper method to print the list containg data about all the iterations"""
        table = Table(title="Quick Sort steps")
        table.add_column("Iteration", justify="center", style="cyan")
        table.add_column("Pivot", justify="center", style="cyan")
        table.add_column("Array in consideration", justify="center", style="magenta", no_wrap=False)
        table.add_column("Array", justify="center", style="magenta", no_wrap=False)

        for iteration in list_of_iterations:
            iter_ = str(iteration[0])
            pivot = str(iteration[1])
            array_in_cons = str(iteration[2])
            array = str(iteration[3])
            table.add_row(iter_, pivot, array_in_cons, array)

        console = Console()
        console.print(table)

    def __eval_helper(self, reverse, pivot, iterations):
        """Helper method for 'evaluate' method

        Evaluating time of ascending quick sort algorithm. Takes in the
        'iterations' provided by the user and performs sorting that many times.

        Args:
            iterations (int): Number of times to perform sorting on this algo
            reverse (bool): check if user wants to reverse the list

        Returns:
            timing_list (list): A list of time taken for fully sorting the
                                list 'iterations' number of times
        """
        timing_list = []
        steps = False
        while iterations:

            timer = Timer()
            timer.start()

            self.__sort_it(reverse, steps, pivot, eval_=True)

            stop = timer.stop()
            timing_list.append(stop)

            iterations -= 1

        return timing_list

    def sort(self, reverse=False, steps=False, pivot="first"):
        """Performs quicksort (lomuto partiton scheme) on the list
        provided by the user.

        Args:
            reverse (bool): Optional; (default: False)
                            If True, sorts the list in descending order
            steps (bool): Optional; (default: False)
                            If set to True, shows iteration of each pass of
                            quicksort on the list

        Returns:
            sorted_list (list): sorted list
        """
        pivot = pivot.lower()

        _sorted_object = self.__sort_it(reverse, steps, pivot)

        # the sorted list is the last list of the last element of
        # sorted obect
        return _sorted_object[-1][-1]

    def evaluate(self, reverse=False, pivot="first", iterations=1):
        """Prints the time taken to perform quick sort in nanoseconds and
        seconds to the console.

        Set optional parameter 'iterations' to the number of times you want to
        perform quick sort on the list. After every iteration, the list is reset to
        it's original unsorted state.

        Set optional parameter 'reverse' to True to sort the list in descending order.

        Args:
            reverse (bool): Optional; (default: False)
                            If True, sorts the list in descending order
            iterations (int): Optional; (default: 1)
                              Number of times to perform quick sort on list

        Raises:
            TypeError: When user inputs anything other than an int for iteration
        """

        if not isinstance(iterations, int):
            raise TypeError('Iterations can only be int datatype')

        pivot = pivot.lower()

        _timing_list = self.__eval_helper(reverse, pivot, iterations)

        _minimum_time = min(_timing_list)
        _maximum_time = max(_timing_list)
        _average_time = int(sum(_timing_list) / iterations)

        _eval_dict = {
            "Minimum Time": _minimum_time,
            "Maximum Time": _maximum_time,
            "Average Time": _average_time
        }

        return super()._print_evaluate(_eval_dict, "Quick Sort")

    def visualize(self, reverse=False, interval=50, pivot="first"):
        """Shows a visualization using matplotlib of quick sort performed on
        the list user passed.

        Set optional parameter 'interval' to change the delay between frames
        in milliseconds.

        Args:
            reverse (bool): Optional; (default: False)
                            If True, sorts the list in descending order
            interval (int): Optional; (default: 50)
                            Delay between frames in milliseconds

        Raises:
            TypeError: An error when user inputs anything other than int for
                       interval
        """
        if not isinstance(interval, int):
            raise TypeError('Interval can only be int datatype')

        _vis_list = copy.deepcopy(self._datalist)

        animate_algorithm("Quick Sort", _vis_list, self.__quicksort(_vis_list, 0, len(_vis_list) - 1, pivot, reverse, vis=True), interval, operations=True)

    @classmethod
    def info(cls):
        """Class method that provides information on quick sort."""
        path_to_information = "algovis/sorting/_markdown_files/quicksort.md"
        return super()._print_info(path_to_information)

    @classmethod
    def code(cls):
        my_code = """
        def partition(arr, low, high):
            # pivot
            pivot = arr[high]
            # Index of smaller element
            i = (low - 1)
            for j in range(low, high):

                # If current element is smaller than or
                # equal to pivot
                if (arr[j] <= pivot):

                    # increment index of smaller element
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return (i + 1)


        def quickSort(arr, low, high):
            if (low < high):
                pi = partition(arr, low, high)

                # Separately sort elements before
                # partition and after partition
                quickSort(arr, low, pi - 1)
                quickSort(arr, pi + 1, high)

        # To give users choice of pivot, the quicksort implemented in this library
        # is slightly different but uses lomuto partiton
        """
        return super()._print_code(my_code)
