from ._base_class import BaseClass

# TODO
# sort
# reverse sort
# iterations
# evaluate
# visualize


class BubbleSort(BaseClass):
    """ 
    In Bubble Sort  we look at pairs of adjacent elements in an array, 
    one pair at a time, and swap their positions if the first element is
    larger than the second, or simply move on if it isn't.
    """

    def __init__(self, datalist):
        super().__init__(datalist)
