from ._base_class import BaseClass

import copy

# TODO
# iterations
# evaluate
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

    def _ascending_sort(self):

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

        return _asc_list

    def _descending_sort(self):

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

        return _desc_list

    def sort(self, reverse=False):
        if reverse:
            _desc_sorted = BubbleSort._descending_sort(self)
            return _desc_sorted
        else:
            _asc_sorted = BubbleSort._ascending_sort(self)
            return _asc_sorted

    def iterations(self):
        pass
