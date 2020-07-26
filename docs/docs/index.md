# Algovis

Algovis is a python library made for visualizing algorithms

Currently the library has

#### Sorting

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort

#### Searching
- Linear Search
- Binary Search


### Example

``` python
# importing the sorting module
from algovis import sorting

#importing the random module for shuffling the list
import random

# creating a list of integers from 1 to 100
my_list = [i + 1 for i in range(100)]

# shuffling the list using random module
random.shuffle(my_list)

# creating an oject of the BubbleSort class and passing
# the list
bs_object = sorting.BubbleSort(my_list)

#calling the visualize method
bs_object.visualize(interval=100)

```

![gif](https://media.giphy.com/media/ieb13rrmvVWC02zmI8/giphy.gif)
