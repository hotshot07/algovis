Every module in the sorting package has these methods

To get started, import the package
```md
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

***

## *info()*

```md
Method that provides information about the sorting algorithm
```

***


## *code()*

```md
Method that prints the python function for the sorting algorithm in console
```
