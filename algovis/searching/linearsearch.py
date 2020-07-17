from ._base_class_search import BaseClass
from ._timer import Timer

from rich.console import Console
from rich.table import Table
import copy

class LinearSearch(BaseClass):

    def __init__(self, datalist):
        super().__init__(datalist)
        self.__datalist = datalist

    def __search_helper(self, number, steps):
        search_list = copy.deepcopy(self.__datalist)

        if steps:
            search_dict = {}
            string_num = ""
            for index, value in enumerate(search_list):
                string_num = string_num + str(value) + " "
                search_dict[index] = string_num
                if value == number:
                    search_dict["[bold green] FOUND [/bold green] "] = f"[bold green]FOUND {number} at index {index}[/bold green]"
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

            return search_str, 0

    def __print_steps(self, step_dict):
        table = Table(title=" Linear search steps")
        table.add_column("At index", justify="center", style="cyan")
        table.add_column("List", style="magenta", no_wrap=False)

        for iteration, step_list in step_dict.items():
            table.add_row(str(iteration), str(step_list))

        console = Console()
        console.print(table)

    def search(self, number, steps=False):

        _search_result = self.__search_helper(number, steps)

        if steps:
            return self.__print_steps(_search_result)
        console = Console()
        return console.print(_search_result)

    def evaluate(self, number, iterations=1):

        _eval_list = copy.deepcopy(self.__datalist)
        _length_of_list = len(_eval_list)

        _timing_list = []

        _eval_iter = iterations

        while _eval_iter:
            timer = Timer()
            timer.start()

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

        print()
        self.search(number, steps=False)
        print()
        return super()._print_evaluate(_eval_dict, "Linear Search")

    @classmethod
    def info(cls):
        _path_to_information = "algovis/searching/_markdown_files/linearsearch.md"
        super()._print_info(_path_to_information)

    @classmethod
    def code(cls):
        ls_code = """ 
        for value in listi:
            print(value)
        """
        super()._print_code(ls_code)
