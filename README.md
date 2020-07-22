[![CodeFactor](https://www.codefactor.io/repository/github/hotshot07/algovis/badge/master?s=197e9c6e50413744c0a2c43785a6dee096ee1a4d)](https://www.codefactor.io/repository/github/hotshot07/algovis/overview/master) ![PyPI](https://img.shields.io/pypi/v/algovis) [![Downloads](https://pepy.tech/badge/algovis)](https://pepy.tech/project/algovis) <!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/algovis) --> ![GitHub last commit](https://img.shields.io/github/last-commit/hotshot07/algovis) ![PyPI - License](https://img.shields.io/pypi/l/algovis) ![Twitter Follow](https://img.shields.io/twitter/follow/gamesetmatch07?style=social) [![Netlify Status](https://api.netlify.com/api/v1/badges/f4cede18-f2c6-4299-abc1-92b8a8ef9995/deploy-status)](https://app.netlify.com/sites/algovisdocs/deploys)

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

#### Visualize method

```python
# import the sorting module from library
from algovis import sorting

# importing random library to fill it a list with random integers
import random

# Making a list of 20 random integers in range of 0 to 100
# using list comprehension 
my_list = [i+1 for i in range(100)]

# shuffling the list using random module
random.shuffle(my_list)

# Making a BubbleSort class object
bs_object = sorting.BubbleSort(my_list)

# calling the visualize method
bs_object.visualize(interval= 100)
```
##### Output
![gif](https://media.giphy.com/media/j3nLvYXv8BIlBkrcAq/giphy.gif)




#### Sort method

```python
# lets work on a shorter example now
my_list = [i + 1 for i in range(10)]

# shuffling the list using random module
random.shuffle(my_list)

#making a quicksort object
qs_object = sorting.QuickSort(my_list)

#sorting in reverse with steps
qs_object.sort(steps = True, reverse = True, pivot = "first")

#you can see the pivot placed correctly in the 'array in consideration' column
```
###### Output
![qs-sort](img/qs-steps.png)





#### Evaluate method
```python
# Making a BubbleSort class object
bs_object = sorting.BubbleSort(my_list)

# calling the evaluate method
# parameters [iterations = 1, reverse = False]
bs_object.evaluate(iterations = 100)
```
###### Output
![eval-img](img/bs-eval.png)




#### Info method
```python
#assuming you already have any sorting object, just call
bs_object.info()
```
###### Output
![info-img](img/bs-info.png)





#### code method
```python
#assuming you already have any sorting object, just call
bs_object.code()
```
###### Output
![code-img](img/bs-code.png)




My terminal config is iTerm2 + ohmyzsh + powerlevel10k with dark backgroud. Colors may appear different in your terminal output. It's recommended to change the terminal color to something darker

### Built With

* [Poetry](https://python-poetry.org/) - Python packaging and dependency management tool
* [Matplotlib](https://pypi.org/project/matplotlib/) - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.  
* [Rich](https://pypi.org/project/rich/) - Rich is a Python library for rich text and beautiful formatting in the terminal.

### Doumentation
The documentation is built with MKdocs using material theme and is hosted on netlify. You can access is from [here](https://algovisdocs.netlify.app/) 

### Author

* **Mayank Arora** *(hotshot07)* 

### Acknowledgements
* my caffeine addiction

### License

This project is licensed under the GNU Affero General Public License v3 (AGPL-3.0) - see the [LICENSE](LICENSE) file for details


    [Last updated on 17th July, 2020]