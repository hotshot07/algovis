"""Linear search module in searching package.

The module is used to demonstrate the working of linear search algorithm

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
    search_object = searching.LinearSearch(list)
    search_object.search(7)
"""
import copy

from rich.console import Console
from rich.table import Table

from ._base_class_search import BaseClass
from ._timer import Timer
from ._animate_search import _AnimateLinearSearch


class LinearSearch(BaseClass):
    """LinearSearch class which contains methods for analyzing linear search.

    Attributes:
        _datalist (list): List of ints provided by the user
    """

    def __init__(self, datalist):
        """Initializes LinearSearch class with datalist.
        Args:
            datalist (list): The list provided by the user"""
        super().__init__(datalist)
        self._datalist = datalist

    def __search_helper(self, number, steps):
        """Helper method to perform search.

        It makes a deepcopy of the datalist to prevent overrides. If the optional
        steps arguemt is true it returns a dict of all the iterations else it returns
        a f-string in 'rich' format

        Args:
            number (int): The number that we have to search
            steps (bool): bool to check if we have to print number of steps

        Returns:
            If steps is true, a dictionary is retured else a string is returned

            search_dict (dict): A dictionary of iterations mapped to where
                                search is in that iteration
            search_str (str): f-string in rich format that is printed to the
                              console
        """
        search_list = copy.deepcopy(self._datalist)

        if steps:
            search_dict = {}
            string_num = ""
            for index, value in enumerate(search_list):
                string_num = string_num + str(value) + " "
                search_dict[index] = string_num
                if value == number:
                    search_dict["[bold green] FOUND [/bold green]"] = f"[bold green]FOUND {number} at index {index}[/bold green]"
                    break

                elif index == len(search_list) - 1 and search_list[index] != number:
                    search_dict["[bold red]NOT FOUND[/bold red]"] = f"[bold red] {number} NOT FOUND in this list [/bold red]"
                    break

            return search_dict

        else:
            search_str = ""
            for index, value in enumerate(search_list):
                if value == number:
                    search_str = f"[bold green]FOUND {number} at index {index}[/bold green]"
                    break

            if not search_str:
                search_str = f"[bold red]{number} NOT FOUND in this list [/bold red]"

            return search_str

    def __print_steps(self, step_dict):
        """Helper method to print the 'search_dict' to console

        Steps are printed using the rich.table module

        Args:
            step_dict (dict): The dict to be printed
        """

        table = Table(title=" Linear search steps")
        table.add_column("At index", justify="center", style="cyan")
        table.add_column("List", style="magenta", no_wrap=False)

        for iteration, step_list in step_dict.items():
            table.add_row(str(iteration), str(step_list))

        console = Console()
        console.print(table)

    def search(self, number, steps=False):
        """Searches if number is in the list and prints the result to the console.

        Set optional parameter 'steps' to True if you want to print the iterations
        table to console

        Args:
            number (int): The number to be searched
            steps (bool): Optional; (default: False)
        """

        # _search_result can be either dict or str
        _search_result = self.__search_helper(number, steps)

        # if steps is True, means it's a dict and we pass it to __print_steps
        # else we just print it
        if steps:
            return self.__print_steps(_search_result)
        console = Console()
        return console.print(_search_result)

    def evaluate(self, number, iterations=1):
        """Performs linear search on the list and prints the result to the
        console.

        Set optional parameter 'iterations' to the number of times you want to
        perform linear search on the list

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
        _length_of_list = len(_eval_list)
        _timing_list = []

        _eval_iter = iterations

        while _eval_iter:
            # instantiating the timer
            timer = Timer()
            timer.start()

            # stopping it only when number is found or we have reached end
            # of the list and havent found the number
            for _index, _value in enumerate(_eval_list):
                if _value == number:
                    _stop = timer.stop()
                    _timing_list.append(_stop)
                    break
                elif _index == _length_of_list - 1:
                    _stop = timer.stop()
                    _timing_list.append(_stop)
                    break

            _eval_iter -= 1

        _minimum_time = min(_timing_list)
        _maximum_time = max(_timing_list)
        _average_time = int(sum(_timing_list) / iterations)

        _eval_dict = {
            "Minimum Time": _minimum_time,
            "Maximum Time": _maximum_time,
            "Average Time": _average_time
        }

        # print statements for better formatting
        print()
        self.search(number, steps=False)
        print()

        # calling the function to print the dictionary
        return super()._print_evaluate(_eval_dict, "Linear Search")

    def visualize(self, number, interval=100):
        """Shows a visualization using matplotlib of linear search performed on
        the list user passed.

        Set optional parameter 'interval' to change the delay between frames
        in milliseconds.

        Args:
            number (int): The number to be searched
            interval (int): Optional; (default: 100)
                            Delay between frames in milliseconds

        Raises:
            TypeError: An error when user inputs anything other than an int for number
                       or interval
        """
        if not isinstance(number, int):
            raise TypeError('Number can only be int datatype')

        if not isinstance(interval, int):
            raise TypeError('Interval can only be int datatype')

        # Instantiating the AnimateLinearSearch class whose init method calls the
        # AnimateAlgorithm function which performs the animation

        # ISSUE: It gets extremely slow on values more than 25
        # any way to optimize??
        _AnimateLinearSearch(self._datalist, number, interval, "Linear Search")

    @classmethod
    def info(cls):
        """Class method that provides information on linear search."""
        _path_to_information = "algovis/searching/_markdown_files/linearsearch.md"
        super()._print_info(cls, _path_to_information)

    @classmethod
    def code(cls):
        """Class method that prints the function for linear search algorithm in console."""
        ls_code = """
        # function for linear search
        # returns the index of the element to search
        # else returns -1
        def linear_search(array,x):

            for index, number in enumerate(array):
                if number == x:
                    return index

            #if number is not found, we return -1
            return -1
        """
        super()._print_code(cls, ls_code)
