import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MaxNLocator


def __update_fig(passed_list, rects, iteration, text, operations):
    for rect, val in zip(rects, passed_list):
        rect.set_height(val)
    iteration[0] += 1
    if operations:
        text.set_text(f"# of operations: {iteration[0]}")
    else:
        text.set_text(f"# of iterations: {iteration[0]}")

def AnimateAlgorithm(title, passed_list, passed_generator, interval, operations=False):

    plt.style.use('dark_background')

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.set_title(title)

    ax.set_xlim(0, len(passed_list))

    ax.set_ylim(0, int(1.05 * max(passed_list)))

    # ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    bar_rects = ax.bar(range(len(passed_list)), passed_list, align="center")

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

    anim = animation.FuncAnimation(fig, func=__update_fig,
                                   fargs=(bar_rects, iteration, text, operations), frames=passed_generator, interval=interval,
                                   repeat=False)

    plt.show()
