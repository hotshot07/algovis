from ._base_class import BaseClass
from ._timer import Timer
from ._animation import AnimateAlgorithm

from rich.console import Console
from rich.table import Table

import copy
import random


class QuickSort(BaseClass):
    def __init__(self, datalist):
        super().__init__(datalist)
        self.__datalist = datalist

    def __repr__(self):
        return f'algovis.sorting.quicksort.QuickSort({self.__datalist})'

    def __choose_pivot(self, arr, start, end, choice):

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

                # if the current element is smaller or equal to pivot,
                # shift it to the left side of the partition.
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

    def __sort_it(self, reverse, steps, pivot, eval_=False):

        if not eval_:
            passed_list = copy.deepcopy(self.__datalist)

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
            passed_list = copy.deepcopy(self.__datalist)

            for elem_pivot, array_in_cons, array in self.__quicksort(passed_list, 0, len(passed_list) - 1, pivot, reverse):
                pass

            return

    def __print_steps_quick(self, list_of_iterations):
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
        pivot = pivot.lower()

        _sorted_object = self.__sort_it(reverse, steps, pivot)
        return _sorted_object[-1][-1]

    def evaluate(self, reverse=False, pivot="first", iterations=1):
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
        _vis_list = copy.deepcopy(self.__datalist)

        AnimateAlgorithm("Quick Sort", _vis_list, self.__quicksort(_vis_list, 0, len(_vis_list) - 1, pivot, reverse, vis=True), interval, operations=True)

    @classmethod
    def info(cls):
        path_to_information = "algovis/sorting/_markdown_files/bubblesort.md"
        return super()._print_info(path_to_information)

    @classmethod
    def code(cls):
        my_code = """

        """

        return super()._print_code(my_code)
