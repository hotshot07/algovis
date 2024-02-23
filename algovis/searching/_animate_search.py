"""Helper animation module in searching package.

This module contains 2 classes, AnimateBinarySearch and AnimateLinearSearch
which contain methods that help in producing the visulization. These classes
are exported to respective modules and when instantiated, the self method
calls the animate_algorithm function(each class has it's own).

Read more about FuncAnimation here
https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MaxNLocator

import time


class _AnimateBinarySearch():
    """Class to animate binary search

    Arrtibutes:
        color_list (list): list that detemines color of each bar

    Methods:
        animate_algorithm: Initialises the figure and calls the animation
        update_fig: Function called by animation.FuncAnimation to update the
                    figure

    Generators:
        color_maker: It's called by animation.FuncAnimation that yields
                     the first paramenter being used in update_fig. Yields
                     the index of where the search is and an integer respresenting
                     if we have found the number

        binary_search: Generator called by color_maker to perform binary search on
                       passed list. Yields a tuple of tuple of (int, int, int) which
                       are indices of (low, mid, high)
    """

    def __init__(self, passed_list, number, interval, title):
        """Instantiating the class.

        Args:
            passed_list (list): The list provided by the user
            number (int): The number we have to search
            interval (int): delay between frames in milliseconds
        """
        self.color_list = ['w'] * len(passed_list)

        self.animate_algorithm(passed_list, number, interval, title)

    def update_fig(self, tup, ax, passed_list, fig, low_text, mid_text, high_text):
        """Method called by animation.FuncAnimation that updates the figure for
        each frame.

        Args:
            tup (int, int, int): Tuple of color_list and tuple returned by color_maker
            ax : Matplotlib axes object
            passed_list (list): The list provided by the user
            low_text (str): setting the low text in every frame
            mid_text (str): setting the mid text in every frame
            high_text (str): setting the high text in every frame
        """

        fig.set_tight_layout(True)

        if tup[0] == -1:
            ax.bar(range(len(passed_list)), passed_list, align="edge", color=['w'] * len(passed_list))
            low_text.set_text(f"low: Not Found")
            mid_text.set_text(f"mid: Not Found")
            high_text.set_text(f"high: Not Found")
        else:
            ax.bar(range(len(passed_list)), passed_list, align="edge", color=self.color_list)
            low_text.set_text(f"low: {passed_list[tup[0]]}")
            mid_text.set_text(f"mid: {passed_list[tup[1]]}")
            high_text.set_text(f"high: {passed_list[tup[2]]}")

    def binary_search(self, arr, number):
        """Method called by color_maker to search list

        Args:
            arr (list): The list provided by the user
            number (int): The number we have to search

        Yields:
            Tuple of (int, int, int) which are indices of low, mid and high
        """
        arr = sorted(arr)
        low = 0
        high = len(arr) - 1
        mid = 0

        # the first value is never shown for some reason so
        # yielding a dummy value
        yield low, mid, high

        while low <= high:
            mid = (high + low) // 2
            yield low, mid, high

            if mid == high or mid == low:
                return

            if arr[mid] < number:
                low = mid + 1
            elif arr[mid] > number:
                high = mid - 1
            else:
                yield low, mid, high
                return
        yield -1, -1, -1

    def color_maker(self, arr, number):
        """Generator called by animation.FuncAnimation that yields the first
        paramenter being used in update_fig.

        Args:
            arr (list): The list provided by the user
            number (int): The number we have to search

        Yields:
            tup (tuple): Tuple returned by binary_search
        """
        for tup in self.binary_search(arr, number):
            low = tup[0]
            mid = tup[1]
            high = tup[2]
            self.color_list[low] = 'b'
            self.color_list[high] = 'b'
            self.color_list[mid] = 'r'
            yield tup
            self.color_list[low] = 'w'
            self.color_list[mid] = 'w'
            self.color_list[high] = 'w'

    def animate_algorithm(self, passed_list, number, interval, title):
        """Method that initializes the animation

        Args:
            passed_list (list): The list provided by the user
            number (int): The number we have to search
            interval (int): delay between frames in milliseconds
            title(str): Heading of the visualization
        """
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(13, 6.5))

        fig.set_tight_layout(True)
        ax.set_xlim(0, len(passed_list))
        ax.set_ylim(0, int(1.15 * max(passed_list)))
        ax.set_title(title)

        ax.bar(range(len(passed_list)), passed_list, align="edge", color=self.color_list)

        text1 = ax.text(0.02, 0.92, "blue: max and min index \nred: mid index", transform=ax.transAxes)
        low_text = ax.text(0.02, 0.88, "low: ", transform=ax.transAxes)
        mid_text = ax.text(0.02, 0.84, "mid: ", transform=ax.transAxes)
        high_text = ax.text(0.02, 0.80, "mid: ", transform=ax.transAxes)

        ax.set_xlabel('index')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        anim = animation.FuncAnimation(fig, func=self.update_fig,
                                       fargs=(ax, passed_list, fig, low_text, mid_text, high_text), frames=self.color_maker(passed_list, number), interval=interval,
                                       repeat=False)

        plt.show()


class _AnimateLinearSearch():
    """Class to animate Linear Search

    Attributes:
        passed_list (list): The list passed by the user

    Methods:
        animate_algorithm: Initialises the figure and calls the animation
        update_fig: Function called by animation.FuncAnimation to update the
                    figure

    Generators:
        color_maker: Generator called by animation.FuncAnimation that yields
                     the first paramenter being used in update_fig.
    """

    def __init__(self, passed_list, number, interval, title):
        """Instantiating the class.

        Args:
            passed_list (list): The list provided by the user
            number (int): The number we have to search
            interval (int): delay between frames in milliseconds
        """

        self.passed_list = passed_list
        # calling the function and starting the animation
        self.animate_algorithm(number, interval, title)

    def color_maker(self, arr, number, rect_obj_list):
        """Generator called by animation.FuncAnimation that yields the first
        paramenter being used in update_fig.

        Args:
            arr (list): The list provided by the user
            number (int): The number we have to search
            rect_obj_list (list): list of matplotlib bar containers
        Yields:
            index (int): index of where the search is
            integer : based on if we have found the element or not
        """

        # necessary for some reason, the first couple of animations
        # happen together if this statement isn't present
        yield 0, 0

        for index, num in enumerate(arr):
            if num != number:
                if index == len(arr) - 1:
                    rect_obj_list[index].set_color('b')

                    yield index, 0

                    for bar in rect_obj_list:
                        bar.set_color('w')

                    yield index, -1
                    return
                else:
                    rect_obj_list[index].set_color('b')
                    yield index, 0
            else:
                rect_obj_list[index].set_color('r')
                yield index, 1
                return

    def update_fig(self, index_, at_index, value):
        """Method called by animation.FuncAnimation that updates the figure for
        each frame.

        Args:
            index_ (int, int): The tuple returned by color_maker
            at_index (str): setting the text in every frame
            value (str): setting the text in every frame
        """

        at_index.set_text(f"at index: {index_[0]}")
        if index_[1] == -1:
            value.set_text(f"value: NOT FOUND")
        else:
            value.set_text(f"value: {self.passed_list[index_[0]]}")

    def animate_algorithm(self, number, interval, title):
        """Method that initializes the animation

        Args:
            number (int): The number we have to search
            interval (int): delay between frames in milliseconds
            title (str): the title of the animation
        """
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 5))
        fig.set_tight_layout(True)

        ax.set_xlim(0, len(self.passed_list))
        ax.set_ylim(0, int(1.15 * max(self.passed_list)))

        # setting every bar to white
        color_list = ['w'] * len(self.passed_list)
        rects = ax.bar(range(len(self.passed_list)), self.passed_list, align="edge", color=color_list)

        # a list of all the bar containers
        rect_obj_list = rects.get_children()

        # rect_obj_list[5].set_color
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        value = ax.text(0.02, 0.92, "value: ", transform=ax.transAxes)
        at_index = ax.text(0.02, 0.96, "at index: ", transform=ax.transAxes)

        anim = animation.FuncAnimation(fig, func=self.update_fig,
                                       fargs=(at_index, value), frames=self.color_maker(self.passed_list, number, rect_obj_list), interval=interval,
                                       repeat=False)

        # # code for saving the animation Future feature?
        # Writer = animation.writers['ffmpeg']
        # writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=50000)
        # anim.save(f"{title.split()[0]}.mp4", writer=writer)

        plt.show()
