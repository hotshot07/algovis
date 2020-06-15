from ._base_class import BaseClass
from ._timer import Timer
# from ._animation import *
import copy

# To be shifted to _animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random


class BubbleSort(BaseClass):
    """
    In Bubble Sort  we look at pairs of adjacent elements in an array,
    one pair at a time, and swap their positions if the first element is
    larger than the second, or simply move on if it isn't.
    """

    def __init__(self, datalist):
        super().__init__(datalist)
        self._datalist = datalist

    def __ascending_sort_algo(self):
        _asc_list = copy.deepcopy(self._datalist)
        _length_of_list = len(_asc_list)
        _has_swapped = True
        _number_of_iterations = 0

        while _has_swapped:
            _has_swapped = False

            for i in range(_length_of_list - _number_of_iterations - 1):
                if _asc_list[i] > _asc_list[i + 1]:
                    _asc_list[i], _asc_list[i + 1] = _asc_list[i + 1], _asc_list[i]
                    _has_swapped = True

            _number_of_iterations += 1
            yield _asc_list

    def __descending_sort_algo(self):
        _desc_list = copy.deepcopy(self._datalist)
        _length_of_list = len(_desc_list)
        _has_swapped = True
        _number_of_iterations = 0

        while _has_swapped:
            _has_swapped = False

            for i in range(_length_of_list - _number_of_iterations - 1):
                if _desc_list[i] < _desc_list[i + 1]:
                    _desc_list[i], _desc_list[i + 1] = _desc_list[i + 1], _desc_list[i]

                    _has_swapped = True

            _number_of_iterations += 1
            yield _desc_list

    def __sort_it(self, reverse, steps):
        _iteration_dict = {}
        iterations = 0

        if not reverse:
            for _yielded_list in self.__ascending_sort_algo():
                iterations += 1
                _iteration_dict[iterations] = copy.deepcopy(_yielded_list)
        else:
            for _yielded_list in self.__descending_sort_algo():
                iterations += 1
                _iteration_dict[iterations] = copy.deepcopy(_yielded_list)

        if steps:
            print()
            print("Iteration    List")
            for _iter, _list in _iteration_dict.items():
                print("     " + str(_iter) + "       " + str(_list))

        return _iteration_dict

    def _time_eval_asc(self, iterations):
        _time_list = copy.deepcopy(self._datalist)
        _length_of_list = len(_time_list)
        _timing_list = []

        while iterations:
            _has_swapped = True
            _number_of_iterations = 0

            timer = Timer()
            timer.start()

            while _has_swapped:
                _has_swapped = False

                for i in range(_length_of_list - _number_of_iterations - 1):
                    if _time_list[i] > _time_list[i + 1]:
                        _time_list[i], _time_list[i + 1] = _time_list[i + 1], _time_list[i]

                        _has_swapped = True

                _number_of_iterations += 1

            stop = timer.stop()
            _timing_list.append(stop)
            iterations -= 1
            _time_list = copy.deepcopy(self._datalist)

        return _timing_list

    def _time_eval_desc(self, iterations):
        _time_list = copy.deepcopy(self._datalist)
        _length_of_list = len(_time_list)
        _timing_list = []

        while iterations:
            _has_swapped = True
            _number_of_iterations = 0

            timer = Timer()
            timer.start()

            while _has_swapped:
                _has_swapped = False

                for i in range(_length_of_list - _number_of_iterations - 1):
                    if _time_list[i] < _time_list[i + 1]:
                        _time_list[i], _time_list[i + 1] = _time_list[i + 1], _time_list[i]

                        _has_swapped = True

                _number_of_iterations += 1

            stop = timer.stop()
            _timing_list.append(stop)
            iterations -= 1
            _time_list = copy.deepcopy(self._datalist)

        return _timing_list

    def sort(self, reverse=False, steps=False):
        _sorted_object = self.__sort_it(reverse, steps)
        return _sorted_object

    def evaluate(self, reverse=False, iterations=1):
        if reverse:
            _timing_list = BubbleSort._time_eval_desc(self, iterations)
        else:
            _timing_list = BubbleSort._time_eval_asc(self, iterations)

        _minimum_time = str("{:.10f}s".format(min(_timing_list)))
        _maximum_time = str("{:.10f}s".format(max(_timing_list)))
        _average_time = str("{:.10f}s".format(sum(_timing_list) / iterations))

        eval_dict = {
            "Minimum Time:": _minimum_time,
            "Maximum Time:": _maximum_time,
            "Average Time:": _average_time
        }
        return eval_dict

    def _anim_algo_gen(my_list):
        length_of_list = len(my_list)
        has_swapped = True
        number_of_iterations = 0

        while has_swapped:
            has_swapped = False

            for i in range(length_of_list - number_of_iterations - 1):
                if my_list[i] > my_list[i + 1]:
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                    has_swapped = True

            number_of_iterations += 1
            yield my_list

    def _update_fig(_vis_list, rects, iteration, text):
        for rect, val in zip(rects, _vis_list):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    def visualize(self):
        _vis_list = copy.deepcopy(self._datalist)
        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        ax.set_title("Bubble Sort")
        bar_rects = ax.bar(range(len(_vis_list)), _vis_list, align="edge")
        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
        iteration = [0]
        anim = animation.FuncAnimation(fig, func=BubbleSort._update_fig,
                                       fargs=(bar_rects, iteration, text), frames=BubbleSort._anim_algo_gen(_vis_list), interval=250,
                                       repeat=False)

        plt.show()
