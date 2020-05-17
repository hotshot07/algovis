import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random


class AnimateAlgorithm:
    def __init__(self):
        fig, ax = plt.subplots()

        ax.set_title("Bubble Sort")

        bar_rects = ax.bar(range(len()), my_list, align="edge")

        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

        iteration = [0]

    def update_fig(my_list, rects, iteration):
        for rect, val in zip(rects, my_list):
            rect.set_height(val)
            iteration[0] += 1
            text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects, iteration), frames=bubblesort(my_list), interval=250,
                                   repeat=False)

    plt.show()
