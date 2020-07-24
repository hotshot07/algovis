"""Helper base class module in sorting package.

This module contains the BaseClass class which all the searching algorithms
inherit. Rich library is used to print out to the console
"""

from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
from rich.markdown import Markdown


class BaseClass:
    """Baseclass is a class inherited by every other public searching module

    It contains all the functions that are relevent to every searching module
    super().__init()__ is called by every searching module. It in itself doesn't
    store the datalist provided by the user, just checks it.
    """

    def __init__(self, datalist):
        """Checks the passed object, raises errors otherwise

        Args:
            datalist (list): The list provided by the user

        Raises:
            TypeError: If object passed is not a list or doesn't contain only integers
            ValueError: If the list is empty

        """
        if not isinstance(datalist, list):
            raise TypeError('Parameter must be a list datatype')

        if not datalist:
            raise ValueError('List cannot be empty')

        for _element in datalist:
            if not isinstance(_element, int):
                raise TypeError('Parameter can only contain int datatype')

    def _print_evaluate(self, eval_dict, name):
        """Helper method to print the 'evaluate' dictionary

        Args:
            eval_dict (dict): The dictionary that we pass after evaluating
                              the algorithm
            name (str): gives heading to the table
        """

        table = Table(title=name + " Evaluation")
        table.add_column("Metric", justify="center", style="cyan")
        table.add_column("Time (ns)", style="magenta", justify="center", no_wrap=False)
        table.add_column("Time (sec)", style="magenta", justify="center", no_wrap=False)

        for metric, time_ns in eval_dict.items():
            table.add_row(str(metric), str(time_ns), str("{:.9f}".format(time_ns / 1e9)))

        console = Console()
        console.print(table)

    def _print_info(self, path_to_information):
        """Helper method to print the information in the console using rich markdown

        Args:
            path_to_information (str): path to the markdown file (in _markdown_files folder)
        """
        console = Console()
        with open(path_to_information) as readme:
            information = Markdown(readme.read(), justify="full")

        console.print(information)

    def _print_code(cls, code_str):
        """Helper method to print the code in the console using rich syntax

        Args:
            code_str (str): (doc)string containing code
        """
        syntax = Syntax(code_str, "python", theme="monokai", line_numbers=True)
        console = Console()
        console.print(syntax)
