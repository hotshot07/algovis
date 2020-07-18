![PyPI](https://img.shields.io/pypi/v/algovis) [![CodeFactor](https://www.codefactor.io/repository/github/hotshot07/algovis/badge/master?s=197e9c6e50413744c0a2c43785a6dee096ee1a4d)](https://www.codefactor.io/repository/github/hotshot07/algovis/overview/master) [![Downloads](https://pepy.tech/badge/algovis)](https://pepy.tech/project/algovis) <!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/algovis) --> ![GitHub last commit](https://img.shields.io/github/last-commit/hotshot07/algovis) ![PyPI - License](https://img.shields.io/pypi/l/algovis) ![Twitter Follow](https://img.shields.io/twitter/follow/gamesetmatch07?style=social)

![Algovis](img/algovis_img.PNG?raw=true)

Algovis is a python library made for visualizing algorithms

Currently the library has these algorithms

#### Sorting

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort

#### Searching
- Linear Search
- Binary Search


## Getting Started

### Prerequisites

I would highly suggest making a virtual environment. The main purpose of Python virtual environments is to create an isolated environment for Python projects. You can read more about them [here](https://realpython.com/python-virtual-environments-a-primer/).

```bash
# making a test folder

$mkdir test_algovis

# make it the current directory

$cd test_algovis

# making a virtual environment (you can replace envname with whatever name you like)

$python3 -m venv envname

# activating it

$source envname/bin/activate

```

You can only access algovis inside this virtual environment. To leave this virtualenv, type

```bash
$deactivate
```

### Installing

```bash
$pip3 install algovis
```
### Using the library


```python
# Using bubblesort in algovis

# import the sorting module from library

from algovis import sorting

# importing random library to fill it a list with random integers

import random

# Making a list of 20 random integers in range of 0 to 100

my_list = [random.randint(0, 100) for i in range(20)]

# Making a BubbleSort class object
# It only accepts lists, raises an exception otherwise

bs_object = sorting.BubbleSort(my_list)

```

Every sorting algorithm has 5 methods
* info()
* sort(reverse = False, steps = False)
* evaluate(iterations = 1)
* code()
* visualize(interval = 250)



```python
# bs_object is now an object of the bubblesort class

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

## Built With

* [Poetry](https://python-poetry.org/) - Python packaging and dependency management tool
* [Matplotlib](https://pypi.org/project/matplotlib/) - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.  
* [Rich](https://pypi.org/project/rich/) - Rich is a Python library for rich text and beautiful formatting in the terminal.


<!-- ## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us. -->


## Author

* **Mayank Arora** *(hotshot07)* 

## License

This project is licensed under the GNU Affero General Public License v3 (AGPL-3.0) - see the [LICENSE](LICENSE) file for details


        [Last updated on 17th July, 2020]