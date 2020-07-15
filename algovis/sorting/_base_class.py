# This module contains the functions
# common to all sorting algorithms

# rich library is used to print data in terminal
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
from rich.markdown import Markdown


class BaseClass:
    # checks for the datalist passed
    def __init__(self, datalist):
        if not isinstance(datalist, list):
            raise TypeError('parameter must be a list datatype')

        if not datalist:
            raise ValueError('parameter has invalid value')

        for _element in datalist:
            if not isinstance(_element, int):
                raise TypeError('parameter can only contain int datatype')

    # _print_steps takes in dictionary and prints the table of iterations
    def _print_steps(self, step_dict):
        table = Table(title="Steps")
        table.add_column("Iteration", justify="center", style="cyan")
        table.add_column("List", style="magenta", justify="center", no_wrap=False)

        for iteration, step_list in step_dict.items():
            list_x = " ".join(map(str, step_list))
            table.add_row(str(iteration), str(list_x))
        console = Console()
        console.print(table)

    # _print_steps takes in eval_dict dictionary and prints the different metrics
    def _print_evaluate(self, eval_dict, name):
        table = Table(title=name + " Evaluation")
        table.add_column("Metric", justify="center", style="cyan")
        table.add_column("Time (ns)", style="magenta", justify="center", no_wrap=False)
        table.add_column("Time (sec)", style="magenta", justify="center", no_wrap=False)

        for metric, time_ns in eval_dict.items():
            table.add_row(str(metric), str(time_ns), str("{:.9f}".format(time_ns / 1e9)))

        console = Console()
        console.print(table)

    # takes in path to the markdown file and renders it
    def _print_info(path_to_information):
        console = Console()
        with open(path_to_information) as readme:
            information = Markdown(readme.read(), justify="full")

        console.print(information)

    # takes in code as a string and displays it in terminal
    def _print_code(my_code):
        syntax = Syntax(my_code, "python", theme="monokai", line_numbers=True)
        console = Console()
        console.print(syntax)
