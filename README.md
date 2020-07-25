[![CodeFactor](https://www.codefactor.io/repository/github/hotshot07/algovis/badge/master?s=197e9c6e50413744c0a2c43785a6dee096ee1a4d)](https://www.codefactor.io/repository/github/hotshot07/algovis/overview/master)  ![PyPI](https://img.shields.io/pypi/v/algovis) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/algovis) [![Downloads](https://pepy.tech/badge/algovis)](https://pepy.tech/project/algovis) <!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/algovis) --> ![GitHub last commit](https://img.shields.io/github/last-commit/hotshot07/algovis)  ![PyPI - License](https://img.shields.io/pypi/l/algovis) ![Netlify](https://img.shields.io/netlify/f4cede18-f2c6-4299-abc1-92b8a8ef9995) [![Made by](https://img.shields.io/badge/Made%20by-hotshot07-blue)](https://mackweb.in) [![Twitter Follow](https://img.shields.io/twitter/follow/gamesetmatch07?style=social)](https://twitter.com/elonmusk)

![Algovis](img/algovis_img.PNG?raw=true)

Algovis is a python library made for visualizing algorithms. You can read the documentation [here](https://algovisdocs.netlify.app/)

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

I would highly suggest making a virtual environment. The main purpose of a Python virtual environments is to create an isolated environment for Python projects. You can read more about them [here](https://realpython.com/python-virtual-environments-a-primer/).

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

You can only access algovis inside this virtual environment. To leave this virtual env when you're done trying out the library, type

```bash
$deactivate
```

### Installing

```bash
$pip3 install algovis
```



### Using the library



#### Visualize method

```python
# import the sorting package from library
from algovis import sorting

# importing random module to shuffle the list
import random

# Making a list of 100 integers from 1-100
# using list comprehension
my_list = [i+1 for i in range(100)]

# shuffling the list
random.shuffle(my_list)

# making a BubbleSort class object by passing the shuffled list
bs_object = sorting.BubbleSort(my_list)

# calling the visualize method
bs_object.visualize(interval= 100)
```
##### Output
![gif](https://media.giphy.com/media/SWiSRxnbbHiJ4u90Ye/giphy.gif)




#### Sort method

```python
# lets work on a shorter example now
my_list = [i + 1 for i in range(10)]

# shuffling the list using random module
random.shuffle(my_list)

#making a quicksort object
qs_object = sorting.QuickSort(my_list)

#sorting in reverse with steps
qs_object.sort(pivot = "first", steps = True, reverse = True)

# you can see the pivot placed correctly in the 'array in consideration' column
# the state of whole array at that iteration is shown in 'array' column
```

##### Output
![qs-sort](img/qs-steps.png)




#### Evaluate method
```python
# calling the evaluate method and passing the optional parameter 'iterations'
# the list is sorted 'iterations' number of times and the min, max and average time taken
#to sort the list is returned in form of a formatted table
bs_object.evaluate(iterations = 100)
```
##### Output
![eval-img](img/bs-eval.png)




#### Info method
```python
# This method gives us information about the algorithm
bs_object.info()
```
##### Output
![info-img](img/bs-info.png)




#### code method
```python
# It prints out the function for the algorithm
bs_object.code()
```
###### Output
![code-img](img/bs-code.png)


My terminal config is iTerm2 + ohmyzsh + powerlevel10k with dark backgroud. Colors may appear different in your terminal output. It's recommended to change the terminal color to something darker

### Built With

* [Poetry](https://python-poetry.org/) - Python packaging and dependency management tool
* [Matplotlib](https://pypi.org/project/matplotlib/) - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
* [Rich](https://pypi.org/project/rich/) - Rich is a Python library for rich text and beautiful formatting in the terminal made by @willmcgugan

### Doumentation
The documentation is built with [MKdocs](https://www.mkdocs.org/) using [material](https://squidfunk.github.io/mkdocs-material/) theme and is hosted on netlify. You can read it [here](https://algovisdocs.netlify.app/)

### Author

* **Mayank Arora** *(hotshot07)*

### Acknowledgements
* My 2019 13" base MacBook Pro, which, I realised in the process of making this library is very underpowered

### License

This project is licensed under the GNU Affero General Public License v3 (AGPL-3.0) - see the [LICENSE](LICENSE) file for details