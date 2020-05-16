from ._base_class import BaseClass
from ._timer import Timer
import copy

# TODO
# visualize


class BubbleSort(BaseClass):
    """
    In Bubble Sort  we look at pairs of adjacent elements in an array,
    one pair at a time, and swap their positions if the first element is
    larger than the second, or simply move on if it isn't.
    """

    def __init__(self, datalist):
        super().__init__(datalist)
        self._datalist = datalist

    def _ascending_sort(self, steps):

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

            if steps:
                print(f'Iteration: {_number_of_iterations}')
                print(f'List:', *_asc_list)
                print('\n')

        return _asc_list

    def _descending_sort(self, steps):

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

            if steps:
                print(f'Iteration: {_number_of_iterations}')
                print(f'List:', * _desc_list)
                print('\n')

        return _desc_list

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
        if reverse:
            _desc_sorted = BubbleSort._descending_sort(self, steps)
            return _desc_sorted
        else:
            _asc_sorted = BubbleSort._ascending_sort(self, steps)
            return _asc_sorted

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
