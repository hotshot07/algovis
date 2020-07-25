"""Helper animation module in sorting package.

This module contains 2 functions, animate algorithm and _update fig which are
used for creating the animations. The animate_algorithm is exported to public
sorting modules and parameters are passed to it which help in making the animation.
_update_fig is used to update the figure at every iteration/operation.

Read more about it here
https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MaxNLocator


def _update_fig(passed_list, rects, iteration, text, operations):
    """Method called by animation.FuncAnimation that updates the figure for
    each frame.

        Args:
            passed_list (list): The list yielded by generator which contains heights
                                of the bars
            rects (plt.container.BarContainer): bar container object that is
                                 used to set heghts
            iteration (list): Used to keep track of iterations/operations
            text (plt.text.Text): text displayed on animation
            operations (bool): if true, it dispays operations instead of iterations
                                in the text
    """
    for rect, val in zip(rects, passed_list):
        rect.set_height(val)
    iteration[0] += 1
    if operations:
        text.set_text(f"# of operations: {iteration[0]}")
    else:
        text.set_text(f"# of iterations: {iteration[0]}")


def animate_algorithm(title, passed_list, passed_generator, interval, operations=False):
    """Method that initializes the animation

        Args:
            title (str): Heading of the animation
            passed_list (list): The list provided by the user
            passed_generator (generator): the generator used in animation to
                                          create each frame
            interval (int): delay between frames in milliseconds
            operations (bool): Optional; (default: False)
                                If set to true, it displays operations instead of
                                iterations in the animation text

        Raises:
            ValueError: If the list contains negative numbers it raises this error
    """

    for elem in passed_list:
        if elem < 0:
            raise ValueError("List cannot contain negative elements")

    plt.style.use('dark_background')

    fig, ax = plt.subplots(figsize=(13, 6.5))
    # fig.set_tight_layout(True)
    ax.set_title(title)

    # setting the x and y limits
    ax.set_xlim(0, len(passed_list))
    ax.set_ylim(0, int(1.09 * max(passed_list)))

    # making x axis labels evenly spaced and integers
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    rects = ax.bar(range(len(passed_list)), passed_list, align="edge")

    # the text that'll be changed
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

    anim_sorting = animation.FuncAnimation(fig, func=_update_fig,
                                           fargs=(rects, iteration, text, operations), frames=passed_generator, interval=interval,
                                           repeat=False, save_count=10000)

    # saving figures
    # Writer = animation.writers['ffmpeg']
    # writer = Writer(fps=1, metadata=dict(artist='Me'), bitrate=50000)
    # anim_sorting.save(f"{title.split()[0]}.mp4", writer=writer)

    plt.show()
