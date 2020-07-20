from ._base_class_search import BaseClass
from ._timer import Timer

from rich.console import Console
from rich.table import Table
import copy


class BinarySearch(BaseClass):

    def __init__(self, datalist):
        super().__init__(datalist)
        self.__datalist = sorted(datalist)

    def __search_helper(self, number, steps):
        search_list = copy.deepcopy(self.__datalist)

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

            return f"[bold red]{number} NOT FOUND in this list [/bold red]", 0

    def __print_steps(self, list_of_iterations, result, number):
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

        if result == -1:
            table.add_row(" ", " ", " ", " ", f"[bold red]{number} NOT FOUND in this list [/bold red]")
        else:
            table.add_row(" ", " ", " ", " ", f"[bold green]FOUND {number} at index {index}[/bold green]")

        console = Console()
        console.print(table)

    def search(self, number, steps=False):

        _search_result, result = self.__search_helper(number, steps)

        if steps:
            return self.__print_steps(_search_result, result, number)
        else:
            console = Console()
            return console.print(_search_result)

    def evaluate(self, number, iterations=1):

        _eval_list = copy.deepcopy(self.__datalist)

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
