import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MaxNLocator
import random


class AnimateBinarySearch():
    def __init__(self, passed_list, number, interval):
        self.AnimateAlgorithm(passed_list, number, interval)

    def update_fig(self, color_, ax, passed_list, low_text, mid_text, high_text):
        if color_[1][0] == -1:
            ax.bar(range(len(passed_list)), passed_list, align="edge", color=['w'] * len(passed_list))
            low_text.set_text(f"low: Not Found")
            mid_text.set_text(f"mid: Not Found")
            high_text.set_text(f"high: Not Found")
        else:
            ax.bar(range(len(passed_list)), passed_list, align="edge", color=color_[0])
            low_text.set_text(f"low: {passed_list[color_[1][0]]}")
            mid_text.set_text(f"mid: {passed_list[color_[1][1]]}")
            high_text.set_text(f"high: {passed_list[color_[1][2]]}")

    def binary_search(self, arr, x):
        arr = sorted(arr)
        low = 0
        high = len(arr) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            yield low, mid, high
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                yield low, mid, high
                return
        yield -1, -1, -1

    def color_maker(self, arr, x):
        for tup in self.binary_search(arr, x):
            color_list = []
            for i in range(len(arr)):
                if i in tup:
                    if tup[1] == i:
                        color = "r"
                        color_list.append(color)
                    elif tup[0] == i or tup[2] == i:
                        color = "b"
                        color_list.append(color)
                else:
                    color = "w"
                    color_list.append(color)

            yield color_list, tup

    def AnimateAlgorithm(self, passed_list, x, interval):
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_xlim(0, len(passed_list))
        ax.set_ylim(0, int(1.15 * max(passed_list)))
        color_ = ['w'] * len(passed_list)
        ax.bar(range(len(passed_list)), passed_list, align="edge", color=color_)
        text1 = ax.text(0.02, 0.92, "blue: max and min index \nred: mid index", transform=ax.transAxes)
        low_text = ax.text(0.02, 0.88, "low: ", transform=ax.transAxes)
        mid_text = ax.text(0.02, 0.84, "mid: ", transform=ax.transAxes)
        high_text = ax.text(0.02, 0.80, "mid: ", transform=ax.transAxes)
        ax.set_xlabel('index')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        anim = animation.FuncAnimation(fig, func=self.update_fig,
                                       fargs=(ax, passed_list, low_text, mid_text, high_text), frames=self.color_maker(passed_list, x), interval=interval,
                                       repeat=False)

        plt.show()


class AnimateLinearSearch():

    def __init__(self, passed_list, number, interval):
        self.color_list = ['w'] * len(passed_list)
        self.AnimateAlgorithm(passed_list, number, interval)

    def color_maker(self, arr, x):
        for index, number in enumerate(arr):
            if number != x:
                if index == len(arr) - 1:
                    self.color_list = ['w'] * len(passed_list)
                    yield index, -1
                    return
                else:
                    self.color_list[index] = 'b'
                    yield index, 0
            else:
                self.color_list[index] = 'r'
                yield index, 0
                return

    def update_fig(self, index_, ax, passed_list, at_index, value):
        ax.bar(range(len(passed_list)), passed_list, align="edge", color=self.color_list)
        at_index.set_text(f"At index: {index_[0]}")
        if index_[1] == -1:
            value.set_text(f"value: NOT FOUND")
        else:
            value.set_text(f"value: {passed_list[index_[0]]}")

    def AnimateAlgorithm(self, passed_list, x, interval):
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_xlim(0, len(passed_list))
        ax.set_ylim(0, int(1.15 * max(passed_list)))
        ax.bar(range(len(passed_list)), passed_list, align="edge", color=self.color_list)
        ax.set_xlabel('index')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        at_index = ax.text(0.02, 0.96, "at index: ", transform=ax.transAxes)
        value = ax.text(0.02, 0.92, "value: ", transform=ax.transAxes)

        # Hardcoding if first value in the list is x
        # For some reason the generator and function animation
        # wouldn't work if only one value is yielded and execution is
        # stopped
        if passed_list[0] == x:
            at_index.set_text(f"At index: 0")
            value.set_text(f"value: {x}")
            self.color_list[0] = 'r'
            ax.bar(range(len(passed_list)), passed_list, align="edge", color=self.color_list)
            plt.show()
            return

        # disabling the cache frame data slightly increased the speed of linear search
        # need to optimize this bit further
        anim = animation.FuncAnimation(fig, func=self.update_fig,
                                       fargs=(ax, passed_list, at_index, value), frames=self.color_maker(passed_list, x), interval=interval,
                                       repeat=False, cache_frame_data=False)

        plt.show()
