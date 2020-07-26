Every module in the sorting package has these methods

To get started, import the package
```python
>>> from algovis import sorting
```


## *sort(reverse = False, steps = False)*
```md
Sorts the list

Args:
    reverse (bool): Optional; (default: False)
                        If True, sorts the list in descending order
    steps (bool): Optional; (default: False)
                        If True, shows iteration of each pass of
                        sort on the list

Returns:
    A sorted list
```
Example
```python
>>> my_list = [i+1 for i in range(50)]
>>> # creating an object of BubbleSort class
>>> # other options are InsertionSort, SelectionSort, MergeSort, QuickSort
>>> bs_object = sorting.BubbleSort(my_list)
>>> #calling the sort method
>>> bs_object.sort(reverse = True, steps = True)
```

***

## *evaluate(reverse=False, iterations=1)*

```md
Prints the time taken to perform the sorting operation in nanoseconds and
seconds to the console.

Set optional parameter 'iterations' to the number of times you want to
sort the list. After every iteration, the list is reset to it's original
unsorted state.

Set optional parameter 'reverse' to True to sort the list in descending order.

Args:
    reverse (bool): Optional; (default: False)
                    If True, sorts the list in descending order
    iterations (int): Optional; (default: 1)
                    Number of times to sort the list

```
Example
```python
>>> bs_object.evaluate(iterations = 42)
```
***

## *visualize(reverse=False, interval=250)*

```md
Shows a visualization using matplotlib of sorting algorithm performed on
the list user passed.

Set optional parameter 'interval' to change the delay between frames
in milliseconds.

Args:
    reverse (bool): Optional; (default: False)
                    If True, sorts the list in descending order
    interval (int): Optional; (default: 250)
                    Delay between frames in milliseconds
```
Example
```python
>>> bs_object.visualize(reverse = True, interval = 100)
```

***

> Note: sort, evaluate and visualize methods for QuickSort class have an extra 'pivot' parameter. The default is 'first' as in the first element of the list. It can be either 'first', 'last', 'middle' or "random".

Example:
```python
>>> quick_obj = sorting.QuickSort([i +1 for i in range(100)])
>>> quick_obj.sort(pivot = "random", reverse = True, steps = True)
>>> quick_obj.evaluate(pivot = "last", reverse = "True" )
>>> quick_obj.visualize(pivot = "middle", reverse = "True" )

```
***

## *info()*

```md
Method that provides information about the sorting algorithm

```

Example
```python
>>> bs_object.info()
```


***


## *code()*

```md
Method that prints the python function for the sorting algorithm in console
```

Example
```python
>>> bs_object.code()
```