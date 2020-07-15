# Insertion Sort 

This is an in-place comparison-based sorting algorithm. Here, a sub-list is maintained which is always sorted. For example, the lower part of an array is maintained to be sorted. An element which is to be 'insert'ed in this sorted sub-list, has to find its appropriate place and then it has to be inserted there. The array is searched sequentially and unsorted items are moved and inserted into the sorted sub-list

It is a stable sorting algorithm.

### Time Complexity
* Worst Case: O(n^2)
* Average Case: O(n^2)
* Best Case: O(n)


### Space Complexity
* O(n) total
* O(1) auxiliary