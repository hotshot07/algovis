import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


class AnimateBinarySearch():
    def __init__(self, passed_list, number, interval):
        self.AnimateAlgorithm(passed_list, number, interval)

    def AnimateAlgorithm(self, passed_list, x, interval):
        passed_list = sorted(passed_list)
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.set_xlim(0, len(passed_list))
        ax.set_ylim(0, int(1.08 * max(passed_list)))
        color_ = ['w'] * len(passed_list)
        ax.bar(range(len(passed_list)), passed_list, align="center", color=color_)
        ax.text(0.02, 0.95, "blue: max and min index \nred: mid index", transform=ax.transAxes)
        anim = animation.FuncAnimation(fig, func=self.update_fig,
                                       fargs=(ax, passed_list), frames=self.color_maker(passed_list, x), interval=interval,
                                       repeat=False)

        plt.show()

    def update_fig(self, color_, ax, passed_list):
        ax.bar(range(len(passed_list)), passed_list, align="center", color=color_)

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

            yield color_list
