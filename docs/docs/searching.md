Every module in the searching package has these methods

To get started, import the package
```python
>>> from algovis import searching
```


# *search(number, steps=False)*

```md
Searches the list for the number and prints the result to the console

Set optional parameter 'steps' to True if you want to print the iterations
table to console

Args:
    number(int): The number to be searched
    steps(bool): Optional; (default: False)
```

Example
```python
>>> my_list = [i + 1 for i in range(50)]
>>>  # creating an object of BinarySearch class
>>>  # other options are LinearSearch
>>> bin_search = searching.BinarySearch(my_list)
>>>  # calling the sort method
>>> bin_search.search(42, steps=True)
```

***

# *evaluate(number, iterations=1)*

```md
Prints the time taken to search in nanoseconds and seconds to the console.

Set optional parameter 'iterations' to the number of times you want to
search the list

Args:
    number(int): The number to be searched
    iterations(int): Optional; (default: 1)

```

Example
```python
>>> bin_search.evaluate(24, iterations=100)
```



***

# *visualize(number, interval=1000)*

```md
Shows a visualization using matplotlib of search performed on
the list user passed.

Set optional parameter 'interval' to change the delay between frames
in milliseconds.

Args:
    number(int): The number to be searched
    interval(int): Optional; (default: 1000)
        Delay between frames in milliseconds

```
Example

```python
>>> bin_search.visualize(29, interval = 100)
```


***

# *info()*

```md
Method that provides information about the searching algorithm
```

Example
```python
>>> bin_search.info()
```

***


# *code()*

```md
Method that prints the python function for the searching algorithm in console
```

Example
```python
>>> bin_search.code()
```

