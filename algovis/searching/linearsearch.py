from ._base_class import BaseClass
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

            return search_str

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

        else:
            console = Console()
            return console.print(_search_result)
