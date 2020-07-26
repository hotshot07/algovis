Every module in the sorting package has these functions

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
Example
```md
>>> my_list = [i+1 for i in range(20)]
>>> random.shuffle(my_list)
>>> qs_object = sorting.QuickSort(my_list)
>>>
>>> qs_object.sort(reverse = True)
'20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1'
>>>
>>> qs_object.sort(reverse = True, steps = True)
                                                       Quick Sort steps
┏━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Iteration ┃ Pivot ┃               Array in consideration               ┃                       Array                        ┃
┡━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│     0     │       │ 13 7 8 12 3 4 15 1 2 9 6 19 18 14 10 16 17 11 5 20 │ 13 7 8 12 3 4 15 1 2 9 6 19 18 14 10 16 17 11 5 20 │
│     1     │  13   │ 20 15 19 18 14 16 17 13 2 9 6 8 12 3 10 4 7 11 5 1 │ 20 15 19 18 14 16 17 13 2 9 6 8 12 3 10 4 7 11 5 1 │
│     2     │  20   │                20 15 19 18 14 16 17                │ 20 15 19 18 14 16 17 13 2 9 6 8 12 3 10 4 7 11 5 1 │
│     3     │  15   │                 17 19 18 16 15 14                  │ 20 17 19 18 16 15 14 13 2 9 6 8 12 3 10 4 7 11 5 1 │
│     4     │  17   │                    18 19 17 16                     │ 20 18 19 17 16 15 14 13 2 9 6 8 12 3 10 4 7 11 5 1 │
│     5     │  18   │                       19 18                        │ 20 19 18 17 16 15 14 13 2 9 6 8 12 3 10 4 7 11 5 1 │
│     6     │   2   │             5 9 6 8 12 3 10 4 7 11 2 1             │ 20 19 18 17 16 15 14 13 5 9 6 8 12 3 10 4 7 11 2 1 │
│     7     │   5   │               11 9 6 8 12 10 7 5 3 4               │ 20 19 18 17 16 15 14 13 11 9 6 8 12 10 7 5 3 4 2 1 │
│     8     │  11   │                  12 11 6 8 9 10 7                  │ 20 19 18 17 16 15 14 13 12 11 6 8 9 10 7 5 3 4 2 1 │
│     9     │   6   │                     7 8 9 10 6                     │ 20 19 18 17 16 15 14 13 12 11 7 8 9 10 6 5 3 4 2 1 │
│    10     │   7   │                      10 8 9 7                      │ 20 19 18 17 16 15 14 13 12 11 10 8 9 7 6 5 3 4 2 1 │
│    11     │  10   │                       10 8 9                       │ 20 19 18 17 16 15 14 13 12 11 10 8 9 7 6 5 3 4 2 1 │
│    12     │   8   │                        9 8                         │ 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 3 4 2 1 │
│    13     │   3   │                        4 3                         │ 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 │
└───────────┴───────┴────────────────────────────────────────────────────┴────────────────────────────────────────────────────┘
```
> the output is coloured in your terminal
***

## *evaluate(reverse=False, iterations=1)*

```md
Prints the time taken to perform the sorting operation in nanoseconds and
seconds to the console.

Set optional parameter 'iterations' to the number of times you want to
perform bubble sort on the list. After every iteration, the list is reset to
it's original unsorted state.

Set optional parameter 'reverse' to True to sort the list in descending order.

Args:
    reverse (bool): Optional; (default: False)
                    If True, sorts the list in descending order
    iterations (int): Optional; (default: 1)
                    Number of times to perform bubble sort on list

```

Example
```md
>>> qs_object.evaluate(iterations =10)
          Quick Sort Evaluation
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃    Metric    ┃ Time (ns) ┃ Time (sec)  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ Minimum Time │  162968   │ 0.000162968 │
│ Maximum Time │  235740   │ 0.000235740 │
│ Average Time │  174676   │ 0.000174676 │
└──────────────┴───────────┴─────────────┘
```

***

