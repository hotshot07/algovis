# Selection Sort
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.


### Time Complexity
* Worst complexity: O(n^2)
* Average complexity: O(n^2)
* Best complexity: 0(n^2)


### Space Complexity
Space complexity: O(1)

### Algorithm
```C
function selectionSort(array a)
    for i in 0 -> a.length - 2 do
        maxIndex = i

        for j in (i + 1) -> (a.length - 1) do
            if a[j] > a[maxIndex]
                maxIndex = j

    swap(a[i], a[maxIndex])
```