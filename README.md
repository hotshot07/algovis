![Alogvis]( /algovis_img.PNG?raw=true)

Algovis is a library with which you can learn how to code data structures and algorithms in Python

It will have most of the prominent sorting, searching and graph algorithms with visualisations.

Currently the library has

# Sorting

- Bubble Sort

# Getting Started

I would highly suggest making a virtual environment as this library is still in beta

For making a virtual environment, we can use virtualenv

```python
# installing virtualenv

$pip3 install virtualenv

# making a test folder

$mkdir test

# make it the current directory

$ cd test

# making a virtual env (you can replace envname with whatever name you like)

$virtualenv - p python3 envname

# activating it

$ source envname / bin / activate

# installing algovis

$ pip3 install algovis
```

You can only access algovis inside this virtual environment. To leave this virtualenv, type

```python
$deactivate
```

# Using this library

I have designed the library this way so that supporting making changes to it is easy

```python
# Using bubblesort in algovis

# import the sorting module from library

from algovis import sorting

# importing random library to fill it the list with random integers

import random

# Making a list of 50 random integers in range of 0 to 100

my_list = [random.randint(0, 100) for i in range(50)]

# Making a bubble sort class object
# It only accepts lists, raises an exception otherwise

bs_object = sorting.BubbleSort(my_list)

# bs_object is now an object of the bubblesort class
# The class has 3 functions

# .sort() with 2 optional parameters reverse and steps, both boolean
# reverse sorts the list in descending order and steps shows every iteration
# of the bubble sort algotithm

# default of reverse if False
# default of steps is False
# return type: Dictionary

desc_sort = bs_object.sort(reverse=True, steps=True)

# .evaluate() with 2 optional parameters reverse and iterations
# .evaluate() returns a dictionary giving a dictionary of minimum,
# maximum and average time to sort the list in seconds

# reverse option sorts it in descending order
# default is False

# iterations is the number of times you want to run the algo
# default is 1

eval_algo0 = bs_object.evaluate(iterations=100)

eval_algo1 = bs_object.evaluate(reverse=True, iterations=500)

# .visualize() makes the visualization of the list you gave getting sorted
# in ascending order
# it has one option, reverse which is a boolean

vis_algo = bs_object.visualize(reverse=True)

```

    [Last updated on 16th June 2020]
