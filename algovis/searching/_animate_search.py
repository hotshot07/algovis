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


class _AnimateBinarySearch():
    """Class to animate binary search

    Methods:
        AnimateAlgorithm: Initialises the figure and calls the animation
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

    def __init__(self, passed_list, number, interval):
        """Instantiating the class.

        Args:
            passed_list (list): The list provided by the user
            number (int): The number we have to search
            interval (int): delay between frames in milliseconds
        """
        self.animate_algorithm(passed_list, number, interval)

    def update_fig(self, color_, ax, passed_list, low_text, mid_text, high_text):
        """Method called by animation.FuncAnimation that updates the figure for
        each frame.

        Args:
            color_ (list, (int, int, int)): Tuple of color_list and tuple returned by color_maker
            ax : Matplotlib axes object
            passed_list (list): The list provided by the user
            low_text (str): setting the low text in every frame
            mid_text (str): setting the mid text in every frame
            high_text (str): setting the high text in every frame
        """
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
        while low <= high:
            mid = (high + low) // 2
            yield low, mid, high
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
            A tuple of 'color_list' and 'tup'
            color_list (list): List of all the colors for each index
            tup (tuple): Tuple returned by binary_search
        """
        for tup in self.binary_search(arr, number):
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

    def animate_algorithm(self, passed_list, number, interval):
        """Method that initializes the animation

        Args:
            passed_list (list): The list provided by the user
            number (int): The number we have to search
            interval (int): delay between frames in milliseconds
        """
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
                                       fargs=(ax, passed_list, low_text, mid_text, high_text), frames=self.color_maker(passed_list, number), interval=interval,
                                       repeat=False)

        plt.show()


class _AnimateLinearSearch():
    """Class to animate Linear Search

    Attributes:
        color_list (list): List of colors that determine the color of
                           bars at any point of time

    Methods:
        AnimateAlgorithm: Initialises the figure and calls the animation
        update_fig: Function called by animation.FuncAnimation to update the
                    figure

    Generators:
        color_maker: Generator called by animation.FuncAnimation that yields
                     the first paramenter being used in update_fig. Yields
                     the index of where the search is and an integer respresenting
                     if we have found the number
    """

    def __init__(self, passed_list, number, interval):
        """Instantiating the class.

        Args:
            passed_list (list): The list provided by the user
            number (int): The number we have to search
            interval (int): delay between frames in milliseconds
        """

        # making all white color list
        self.color_list = ['w'] * len(passed_list)

        # calling the function and starting the animation
        self.animate_algorithm(passed_list, number, interval)

    def color_maker(self, arr, number):
        """Generator called by animation.FuncAnimation that yields the first
        paramenter being used in update_fig.

        Args:
            arr (list): The list provided by the user
            number (int): The number we have to search

        Yields:
            index (int): index of where the search is
            integer : based on if we have found the element or not
        """
        for index, num in enumerate(arr):
            if num != number:
                if index == len(arr) - 1:
                    # if we've reached last element, we make everything white
                    self.color_list = ['w'] * len(arr)
                    yield index, -1
                    return
                else:
                    self.color_list[index] = 'b'
                    yield index, 0
            else:
                self.color_list[index] = 'r'
                yield index, 1
                return

    def update_fig(self, index_, ax, passed_list, at_index, value):
        """Method called by animation.FuncAnimation that updates the figure for
        each frame.

        Args:
            index_ (int, int): The tuple returned by color_maker
            ax : Matplotlib axes object
            passed_list (list): The list provided by the user
            at_index (str): setting the text in every frame
            value (str): setting the text in every frame
        """

        ax.bar(range(len(passed_list)), passed_list, align="edge", color=self.color_list)
        at_index.set_text(f"At index: {index_[0]}")
        if index_[1] == -1:
            value.set_text(f"value: NOT FOUND")
        else:
            value.set_text(f"value: {passed_list[index_[0]]}")

    def animate_algorithm(self, passed_list, number, interval):
        """Method that initializes the animation

        Args:
            passed_list (list): The list provided by the user
            number (int): The number we have to search
            interval (int): delay between frames in milliseconds
        """
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_xlim(0, len(passed_list))
        ax.set_ylim(0, int(1.15 * max(passed_list)))
        ax.bar(range(len(passed_list)), passed_list, align="edge", color=self.color_list)
        ax.set_xlabel('index')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        at_index = ax.text(0.02, 0.96, "at index: ", transform=ax.transAxes)
        value = ax.text(0.02, 0.92, "value: ", transform=ax.transAxes)

        # Hardcoding if first value in the list is number we are searching
        # For some reason the generator and funcAnimation
        # wouldn't work if only one value is yielded and execution is
        # stopped
        if passed_list[0] == number:
            at_index.set_text(f"At index: 0")
            value.set_text(f"value: {number}")
            self.color_list[0] = 'r'
            ax.bar(range(len(passed_list)), passed_list, align="edge", color=self.color_list)
            plt.show()
            return

        # disabling the cache frame data slightly increased the speed of linear search
        # need to optimize this bit further
        anim = animation.FuncAnimation(fig, func=self.update_fig,
                                       fargs=(ax, passed_list, at_index, value), frames=self.color_maker(passed_list, number), interval=interval,
                                       repeat=False, cache_frame_data=False)

        plt.show()
