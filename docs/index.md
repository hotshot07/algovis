# Algovis

Algovis is a python library made for visualizing algorithms

Currently the library has 

##### Sorting

- [Bubble Sort](sorting/bubblesort.md)
- [Insertion Sort](sorting/insertionsort.md)
- [Selection Sort](sorting/selectionsort.md)
- [Merge Sort](sorting/mergesort.md)
- [Quick Sort](sorting/quicksort.md)

##### Searching
- [Linear Search](searching/linearsearch.md)
- [Binary Search](searching/binarysearch.md)


### Example

``` python
# importing the sorting module
from algovis import sorting

#importing the random module for shuffling the list
import random

# creating a list of integers from 1-100
my_list = [i + 1 for i in range(100)]

# shuffling the list using random module
random.shuffle(my_list)

# creating an oject of the BubbleSort class and passing
# the list we made
bs_object = sorting.BubbleSort(my_list)

#calling the visualize method 
bs_object.visualize(interval=100)

```

![gif](https://media.giphy.com/media/j3nLvYXv8BIlBkrcAq/source.mp4)
