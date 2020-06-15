import copy


class BubbleSort():

    def __init__(self, datalist):
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

    def __ascending_sort(self):
        _yi_li = []
        iterations = 0
        for _yielded_list in BubbleSort.__ascending_sort_algo(self):
            _yi_li.append(copy.deepcopy(_yielded_list))

        return _yi_li

    def sort(self):
        _asc_sorted = self.__ascending_sort()
        return _asc_sorted


listi = [4, 7, 5, 3, 2, 7, 9, 3, 1]

A = BubbleSort(listi).sort()
print(A)

listi = [6, 2, 4, 2, 6, 3, 7, 9, 7, 5, 3, 1, 5]
A = BubbleSort(listi).sort()
print(A)
