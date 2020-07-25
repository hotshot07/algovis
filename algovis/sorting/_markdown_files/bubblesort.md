# Bubble Sort

In Bubble Sort, we look at pairs of adjacent elements in an array, one pair at a time, and swap their positions if the first element is larger than the second, or simply move on if it isn't.
It is a stable sorting algorithm.


### Time Complexity
* Worst Case: O(n^2)
* Average Case: O(n^2)
* Best Case: O(n)


### Space Complexity
* O(n) total
* O(1) auxiliary


### Algorithm
```C
procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped := false
        for i := 1 to n - 1 inclusive do
            if A[i - 1] > A[i] then
                swap(A[i - 1], A[i])
                swapped = true
            end if
        end for
        n := n - 1
    until not swapped
end procedure
```
