from ._base_sorting import BaseClass
from ._timer import Timer
from ._animation import AnimateAlgorithm
import copy


class MergeSort(BaseClass):
    def __init__(self, datalist):
        super().__init__(datalist)
        self._datalist = datalist

    def __repr__(self):
        return f'algovis.sorting.mergesort.MergeSort({self._datalist})'

    def __ascending_sort_merge_algo(self, passed_list, start, mid, end):
        merged = []
        leftIdx = start
        rightIdx = mid + 1

        while leftIdx <= mid and rightIdx <= end:
            if passed_list[leftIdx] < passed_list[rightIdx]:
                merged.append(passed_list[leftIdx])
                leftIdx += 1
            else:
                merged.append(passed_list[rightIdx])
                rightIdx += 1

        while leftIdx <= mid:
            merged.append(passed_list[leftIdx])
            leftIdx += 1

        while rightIdx <= end:
            merged.append(passed_list[rightIdx])
            rightIdx += 1

        for i, sorted_val in enumerate(merged):
            passed_list[start + i] = sorted_val

        yield passed_list

    def __descending_sort_merge_algo(self, passed_list, start, mid, end):
        merged = []
        leftIdx = start
        rightIdx = mid + 1

        while leftIdx <= mid and rightIdx <= end:
            if passed_list[leftIdx] > passed_list[rightIdx]:
                merged.append(passed_list[leftIdx])
                leftIdx += 1
            else:
                merged.append(passed_list[rightIdx])
                rightIdx += 1

        while leftIdx <= mid:
            merged.append(passed_list[leftIdx])
            leftIdx += 1

        while rightIdx <= end:
            merged.append(passed_list[rightIdx])
            rightIdx += 1

        for i, sorted_val in enumerate(merged):
            passed_list[start + i] = sorted_val

        yield passed_list

    def __merge_algo(self, passed_list, start, end, reverse):
        if end <= start:
            return

        mid = start + ((end - start + 1) // 2) - 1
        yield from self.__merge_algo(passed_list, start, mid, reverse)
        yield from self.__merge_algo(passed_list, mid + 1, end, reverse)
        if not reverse:
            yield from self.__ascending_sort_merge_algo(passed_list, start, mid, end)
        else:
            yield from self.__descending_sort_merge_algo(passed_list, start, mid, end)
        yield passed_list

    # generator passed to visualize method, yields a list after every iteration

    def __animate_sort_it(self, reverse=False):
        passed_list = copy.deepcopy(self._datalist)
        for i in self.__merge_algo(passed_list, 0, len(passed_list) - 1, reverse):
            yield i

    def __sort_it(self, reverse, steps):
        passed_list = copy.deepcopy(self._datalist)
        iteration_dict = {}
        iterations = 0

        # the 0th iteration is basically the passed list
        iteration_dict[iterations] = self._datalist

        for yielded_list in self.__merge_algo(passed_list, 0, len(passed_list) - 1, reverse):
            iterations += 1
            iteration_dict[iterations] = copy.deepcopy(yielded_list)

        if steps:
            super()._print_steps(iteration_dict)

        return iteration_dict

    # for evaluation
    # using https://stackoverflow.com/questions/7063697/why-is-my-mergesort-so-slow-in-python
    # Making mergesort faster
    # I have used this as I wanted the methods above to be 'cleaner'
    # but this one to be as fast as possible
    # breaking the DRY principle as it just wasn't working for some reason
    def __fast_merge_asc(self, array1, array2):
        merged_array = []
        while array1 or array2:
            if not array1:
                merged_array.append(array2.pop())
            elif (not array2) or array1[-1] > array2[-1]:
                merged_array.append(array1.pop())
            else:
                merged_array.append(array2.pop())
        merged_array.reverse()
        return merged_array

    def __fast_merge_desc(self, array1, array2):
        merged_array = []
        while array1 or array2:
            if not array1:
                merged_array.append(array2.pop())
            elif (not array2) or array1[-1] < array2[-1]:
                merged_array.append(array1.pop())
            else:
                merged_array.append(array2.pop())
        merged_array.reverse()
        return merged_array

    def __no_len_ms(self, array, reverse):
        n = len(array)
        if n <= 1:
            return array
        mid = int(n / 2)
        left = array[:mid]
        right = array[mid:]
        if not reverse:
            return self.__fast_merge_asc(self.__no_len_ms(left, reverse), self.__no_len_ms(right, reverse))
        return self.__fast_merge_desc(self.__no_len_ms(left, reverse), self.__no_len_ms(right, reverse))

    def __eval_helper(self, reverse, iterations):
        timing_list = []

        while iterations:
            time_list = copy.deepcopy(self._datalist)

            timer = Timer()
            timer.start()

            self.__no_len_ms(time_list, reverse)

            stop = timer.stop()
            timing_list.append(stop)

            iterations -= 1

        return timing_list

    # sort method calls __sort_it, which works more or less like the ones in bubble
    # or insertion, the difference being that the reverse option is passed to
    # __merge_algo, which decides based on reverse which generator to call
    # __ascending_sort_merge_algo or __descending_sort_merge_algo

    def sort(self, reverse=False, steps=False):
        _sorted_object = self.__sort_it(reverse, steps)
        return list(_sorted_object.values())[-1]

    def evaluate(self, reverse=False, iterations=1):
        _timing_list = self.__eval_helper(reverse, iterations)

        _minimum_time = min(_timing_list)
        _maximum_time = max(_timing_list)
        _average_time = int(sum(_timing_list) / iterations)

        _eval_dict = {
            "Minimum Time": _minimum_time,
            "Maximum Time": _maximum_time,
            "Average Time": _average_time
        }

        return super()._print_evaluate(_eval_dict, "Merge Sort")

    # visualize method in quicksort calls __animate_sort_it

    def visualize(self, reverse=False, interval=250):
        _vis_list = copy.deepcopy(self._datalist)

        AnimateAlgorithm("Merge Sort", _vis_list, self.__animate_sort_it(reverse), interval, operations=True)

    @classmethod
    def info(cls):
        path_to_information = "algovis/sorting/_markdown_files/mergesort.md"
        return super()._print_info(path_to_information)

    @classmethod
    def code(cls):
        my_code = """

        """

        return super()._print_code(my_code)
