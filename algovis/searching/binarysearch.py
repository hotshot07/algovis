"""Binary search module in searching package.

The module is used to demonstrate the working of binary search algorithm

Exported methods:
    search
    evaluate
    visualize
    info
    code

Helper methods:
    __search_helper
    __print_steps

Example usage:
    search_object = searching.Binary(list)
    search_object.search(42)
"""
import copy

from rich.console import Console
from rich.table import Table

from ._base_class_search import BaseClass
from ._timer import Timer
from ._animate_search import _AnimateBinarySearch


class BinarySearch(BaseClass):
    """BinarySearch class which contains methods for analyzing binary search.

    Attributes:
        _datalist (list): List of ints provided by the user
    """

    def __init__(self, datalist):
        """Initializes BinarySearch class with datalist.

        Args:
            datalist (list): The list provided by the user. If the list is unsorted,
                             it is automatically sorted
        """
        super().__init__(datalist)
        self._datalist = sorted(datalist)

    def __repr__(self):
        return f'algovis.searching.binarysearch.BinarySearch({self._datalist})'

    def __search_helper(self, number, steps):
        """Helper method to perform search.

        It makes a deepcopy of the datalist to prevent accidental overrides. If the optional
        steps arguemt is true it returns a tuple of lists of list of all the iterations (multiple values)
        and index of 'number'(if present) else -1.
        Else it returns a f-string in 'rich' format

        Args:
            number (int): The number that we have to search
            steps (bool): Bool to check if we have to print number of steps

        Returns:
            If steps is true, a tuple of (list of lists, index of element) is returned else a tuple of
            (f-string,index of element) is returned. If element is not found, index is -1

            list_of_iterations, index: A tuple of (list of lists, index_of_searched_element)
            f-string, index: A tuple of (f-string, index_of_searched_element)
        """
        search_list = copy.deepcopy(self._datalist)

        if steps:
            list_of_iterations = []
            counter = 0
            left_index = 0
            right_index = len(search_list) - 1

            while left_index <= right_index:
                temp_list = []
                temp_list.append(str(counter))
                temp_list.append(str(left_index))
                temp_list.append(str(right_index))

                middle_index = left_index + (right_index - left_index) // 2

                temp_list.append(str(middle_index))

                temp_list.append(search_list[left_index:right_index + 1])

                list_of_iterations.append(temp_list)

                counter = counter + 1

                if search_list[middle_index] == number:
                    return list_of_iterations, middle_index

                elif search_list[middle_index] < number:
                    left_index = middle_index + 1

                else:
                    right_index = middle_index - 1

            return list_of_iterations, -1

        else:

            left_index = 0
            right_index = len(search_list) - 1

            while left_index <= right_index:

                middle_index = left_index + (right_index - left_index) // 2

                if search_list[middle_index] == number:
                    return f"[bold green]FOUND {number} at index {middle_index}[/bold green]", 0

                elif search_list[middle_index] < number:
                    left_index = middle_index + 1

                else:
                    right_index = middle_index - 1

            return f"[bold red]{number} NOT FOUND in this list [/bold red]", -1

    def __print_steps(self, list_of_iterations, index, number):
        """Helper method to print the list_of_iterations to console.

        Steps are printed using the rich.table module

        Args:
            list_of_iterations (list): A list of lists containing data about every iteration
            index (int): The index of element (number)
            number (int): Element to be searched

        """
        table = Table(title="Binary search steps")
        table.add_column("Iteration", justify="center", style="cyan")
        table.add_column("Left index", justify="center", style="cyan")
        table.add_column("Middle index", justify="center", style="cyan")
        table.add_column("Right index", justify="center", style="cyan")
        table.add_column("List", style="magenta", justify="center", no_wrap=False)

        for iteration in list_of_iterations:
            iter_ = str(iteration[0])
            left_ix = str(iteration[1])
            right_ix = str(iteration[2])
            middle_ix = str(iteration[3])
            list_ = " ".join(str(i) for i in iteration[4])
            table.add_row(iter_, left_ix, middle_ix, right_ix, list_)

        # adding last row based on if we found the number or not
        if index == -1:
            table.add_row(" ", " ", " ", " ", f"[bold red]{number} NOT FOUND in this list [/bold red]")
        else:
            table.add_row(" ", " ", " ", " ", f"[bold green]FOUND {number} at index {index}[/bold green]")

        console = Console()
        console.print(table)

    def search(self, number, steps=False):
        """Performs iterative binary search on the list and prints the result
        to the console.

        Set optional parameter 'steps' to True if you want to print the iterations
        table to console

        Args:
            number (int): The number to be searched
            steps (bool): Optional; (default: False)
        """

        _search_result, index = self.__search_helper(number, steps)

        if steps:
            return self.__print_steps(_search_result, index, number)
        else:
            console = Console()
            return console.print(_search_result)

    def evaluate(self, number, iterations=1):
        """Prints the time taken to perform binary search in nanoseconds and seconds
        to the console.

        Set optional parameter 'iterations' to the number of times you want to
        perform binary search on the list

        Args:
            number (int): The number to be searched
            iterations (int): Optional; (default: 1)

        Raises:
            TypeError: When user inputs anything other than an int for number
                       or iteration
        """

        if not isinstance(number, int):
            raise TypeError('Number can only be int datatype')

        if not isinstance(iterations, int):
            raise TypeError('Iterations can only be int datatype')

        _eval_list = copy.deepcopy(self._datalist)
        _timing_list = []
        _eval_iter = iterations

        while _eval_iter:
            timer = Timer()
            timer.start()

            left_index = 0
            right_index = len(_eval_list) - 1

            while left_index <= right_index:
                middle_index = left_index + (right_index - left_index) // 2

                if _eval_list[middle_index] == number:
                    _stop = timer.stop()
                    _timing_list.append(_stop)
                    break
                elif _eval_list[middle_index] < number:
                    left_index = middle_index + 1
                else:
                    right_index = middle_index - 1

            # if we don't find the number and reach the end
            if _eval_list[middle_index] != number:
                _stop = timer.stop()
                _timing_list.append(_stop)

            _eval_iter -= 1

        _minimum_time = min(_timing_list)
        _maximum_time = max(_timing_list)
        _average_time = int(sum(_timing_list) / iterations)

        _eval_dict = {
            "Minimum Time": _minimum_time,
            "Maximum Time": _maximum_time,
            "Average Time": _average_time
        }

        print()
        self.search(number, steps=False)
        print()

        return super()._print_evaluate(_eval_dict, "Binary Search")

    def visualize(self, number, interval=1000):
        """Shows a visualization using matplotlib of binary search performed on
        the list user passed.

        Set optional parameter 'interval' to change the delay between frames
        in milliseconds.

        Args:
            number (int): The number to be searched
            interval (int): Optional; (default: 1000)
                            Delay between frames in milliseconds

        Raises:
            TypeError: An error when user inputs anything other than int for number
                       or interval
        """
        if not isinstance(number, int):
            raise TypeError('Number can only be int datatype')

        if not isinstance(interval, int):
            raise TypeError('Interval can only be int datatype')

        # Instantiating the AnimateBinarySearch class whose init method calls the
        # AnimateAlgorithm function which performs the animation
        _AnimateBinarySearch(self._datalist, number, interval, "Binary Search")

    @classmethod
    def info(cls):
        """Class method that provides information on binary search."""
        _path_to_information = "algovis/searching/_markdown_files/binarysearch.md"
        super()._print_info(cls, _path_to_information)

    @classmethod
    def code(cls):
        """Class method that prints the function for binary search algorithm in console."""
        bs_code = """
        # iterative binary search
        def binary_search(array, low, mid, high):

            while low <= high:

                mid = low + (high - low)//2

                # Check if x is present at mid
                if array[mid] == x:
                    return mid

                # If x is greater, ignore left half
                elif array[mid] < x:
                    low = mid + 1

                # If x is smaller, ignore right half
                else:
                    high = mid - 1

            # If we reach here, then the element
            # was not present
            return -1
        """
        super()._print_code(cls, bs_code)
