import matplotlib.pyplot as plt
import matplotlib.animation as animation


def __update_fig(passed_list, rects, iteration, text):
    for rect, val in zip(rects, passed_list):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text(f"# of iterations: {iteration[0]}")

def AnimateAlgorithm(title, passed_list, passed_generator, interval):

    plt.style.use('dark_background')

    fig, ax = plt.subplots()

    ax.set_title(title)

    ax.set_xlim(0, len(passed_list))

    ax.set_ylim(0, int(1.07 * max(passed_list)))

    bar_rects = ax.bar(range(len(passed_list)), passed_list, align="edge")

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

    anim = animation.FuncAnimation(fig, func=__update_fig,
                                   fargs=(bar_rects, iteration, text), frames=passed_generator, interval=interval,
                                   repeat=False)

    plt.show()
