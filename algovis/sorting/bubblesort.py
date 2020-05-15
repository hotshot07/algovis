from ._base_class import BaseClass
from ._timer import Timer
import copy

# TODO
# info
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

    def _ascending_sort(self, iterations):

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

            if iterations:
                print(f'Iteration: {_number_of_iterations}')
                print(f'List:', *_asc_list)
                print('\n')

        return _asc_list

    def _descending_sort(self, iterations):

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

            if iterations:
                print(f'Iteration: {_number_of_iterations}')
                print(f'List:', * _desc_list)
                print('\n')

        return _desc_list

    def _time_eval(self, reverse, iterations):
        _time_list = copy.deepcopy(self._datalist)

        _length_of_list = len(_time_list)

        _timing_list = []

        while iterations:

            timer = Timer()
            timer.start()

            _number_of_iterations = 0
            _has_swapped = True

            while _has_swapped:
                _has_swapped = False

                for i in range(_length_of_list - _number_of_iterations - 1):

                    if reverse:
                        if _time_list[i] < _time_list[i + 1]:
                            _time_list[i], _time_list[i + 1] = _time_list[i + 1], _time_list[i]
                            _has_swapped = True
                    else:
                        if _time_list[i] > _time_list[i + 1]:
                            _time_list[i], _time_list[i + 1] = _time_list[i + 1], _time_list[i]
                            _has_swapped = True

                    _number_of_iterations += 1

            stop = timer.stop()

            _timing_list.append(stop)

            iterations -= 1

        return _timing_list

    def sort(self, reverse=False, iterations=False):
        if reverse:
            _desc_sorted = BubbleSort._descending_sort(self, iterations)
            return _desc_sorted
        else:
            _asc_sorted = BubbleSort._ascending_sort(self, iterations)
            return _asc_sorted

    def evaluate(self, reverse=False, iterations=1):
        _timing_list = BubbleSort._time_eval(self, reverse, iterations)

        _timing_list = [str("{:.10f}".format(_elem)) for _elem in _timing_list]
        # _timing_list = [ for _elem in _timing_list]

        # minimum_time = min(_timing_list)
        # maximum_time = max(_timing_list)
        # average_time = sum(_timing_list) / float(iterations)

        return _timing_list
