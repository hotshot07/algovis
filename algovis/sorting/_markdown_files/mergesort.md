# Merge Sort
Merge sort is an efficient, general-purpose, comparison-based sorting algorithm. It is a divide-and-conquer algorithm. An initial array is divided into two roughly equal parts. If the array has an odd number of elements, one of those "halves" is by one element larger than the other.

The subarrays are divided over and over again into halves until you end up with arrays that have only one element each. Then you combine the pairs of one-element arrays into two-element arrays, sorting them in the process. Then these sorted pairs are merged into four-element arrays, and so on until you end up with the initial array sorted.


### Time Complexity
* Worst-case performance:  O(n\*log n)
* Average performance: O(n\*log n)
* Best-case performance: O(n\*log n) typical, O(n) natural variant


### Space Complexity
* Worst-case: О(n) total with O(n) auxiliary

### Algorithm
```C
function merge_sort(list m) is
    // Base case. A list of zero or one elements is sorted, by definition.
    if length of m <= 1 then
        return m

    // Recursive case. First, divide the list into equal-sized sublists
    // consisting of the first half and second half of the list.
    // This assumes lists start at index 0.
    var left := empty list
    var right := empty list
    for each x with index i in m do
        if i < (length of m)/2 then
            add x to left
        else
            add x to right

    // Recursively sort both sublists.
    left := merge_sort(left)
    right := merge_sort(right)

    // Then merge the now-sorted sublists.
    return merge(left, right)

```