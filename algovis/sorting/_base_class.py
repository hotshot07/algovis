# This module contains the functions
# common to sorting algorithms

from rich import print as rprint
from rich.console import Console
from rich.table import Table


class BaseClass:
    def __init__(self, datalist):
        if not isinstance(datalist, list):
            raise TypeError('parameter must be a list datatype')

        if not datalist:
            raise ValueError('parameter has invalid value')

        for _element in datalist:
            if not isinstance(_element, int):
                raise TypeError('parameter can only contain int datatype')

    def _print_evaluate(self, passed_dict):
        table = Table(title="Evaluate")
        table.add_column("Iteration", justify="center", style="cyan")
        table.add_column("List", style="magenta", justify="center", no_wrap=False)

        for iteration, list_x in passed_dict.items():
            list_x = " ".join(map(str, list_x))
            table.add_row(str(iteration), str(list_x))

        console = Console()
        console.print(table)
