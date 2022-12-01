# Sorting algorithms in Python

## List of sorting algorithms

- [Insertion Sort](#insertion-sort)
- [Selection Sort](#selection-sort)
<!-- - [Bubble Sort](#bubble-sort) -->
- [Merge Sort](#merge-sort)
<!-- - [Quick Sort](#quick-sort) -->
<!-- - [Heap Sort](#heap-sort) -->

---

## Insertion Sort

Insertion sort is a sorting algorithm that sorts an array by repeatedly inserting an element from the unsorted part of the array into the sorted part of the array. This type of sorting algorithm is very efficient for small data sets, with time complexity of O(n). However, it is not very efficient for large data sets, with time complexity of O(n^2). Insertion sort is a divide and conquer algorithm. It divides the input array into two halves, sorts the two halves, and then merges the two sorted halves. However, unlike merge sort, insertion sort does not use additional memory space to store the two halves of the array. Instead, it sorts the array in place. Inplace sorting algorithms are more efficient than sorting algorithms that use additional memory space.

### Algorithm (Insertion Sort)

1. Set the index of the unsorted array to 1.
2. While the index of the unsorted array is less than the length of the array:
    1. Set the index of the sorted array to the index of the unsorted array minus 1.
    2. While the index of the sorted array is greater than or equal to 0:
        1. If the element at the index of the sorted array is greater than the element at the index of the unsorted array:
            1. Set the element at the index of the sorted array plus 1 to the element at the index of the sorted array.
            2. Decrement the index of the sorted array.
        2. Else:
            1. Break.
    3. Set the element at the index of the sorted array plus 1 to the element at the index of the unsorted array.
    4. Increment the index of the unsorted array.
3. Return the array.
4. Return the result of calling insertion sort on the array.
5. Return the sorted array.

### Pseudocode (Insertion Sort)

```python
def insertion_sort(array):
    unsorted_index = 1
    while unsorted_index < len(array):
        sorted_index = unsorted_index - 1
        while sorted_index >= 0:
            if array[sorted_index] > array[unsorted_index]:
                array[sorted_index + 1] = array[sorted_index]
                sorted_index -= 1
            else:
                break
        array[sorted_index + 1] = array[unsorted_index]
        unsorted_index += 1
    return array
```

### Example (Insertion Sort)

```python
>>> insertion_sort([5, 4, 3, 2, 1])
[1, 2, 3, 4, 5]
```

### Complexity (Insertion Sort)

| Name | Best | Average | Worst | Memory | Stable | Comments | Data Structure |
| ---- | ---- | ------- | ----- | ------ | ------ | -------- | -------------- |
| Insertion Sort | O(n) | O(n^2) | O(n^2) | O(1) | Yes | - | Array |

### References (Insertion Sort)

- [Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort) - Insertion sort algorithm
- [GeeksforGeeks](https://www.geeksforgeeks.org/insertion-sort/) - Insertion Sort

## Selection Sort

Selection sort is a sorting algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and placing it at the beginning of the unsorted part of the array. This type of sorting algorithm is very efficient for small data sets, with time complexity of O(n^2). However, it is not very efficient for large data sets, with time complexity of O(n^2). Selection sort is a divide and conquer algorithm. It divides the input array into two halves, sorts the two halves, and then merges the two sorted halves. However, unlike merge sort, selection sort does not use additional memory space to store the two halves of the array. Instead, it sorts the array in place. Inplace sorting algorithms are more efficient than sorting algorithms that use additional memory space.

### Algorithm (Selection Sort)

1. Set the index of the unsorted array to 0.
2. While the index of the unsorted array is less than the length of the array minus 1:
    1. Set the index of the minimum element to the index of the unsorted array.
    2. Set the index of the sorted array to the index of the unsorted array plus 1.
    3. While the index of the sorted array is less than the length of the array:
        1. If the element at the index of the sorted array is less than the element at the index of the minimum element:
            1. Set the index of the minimum element to the index of the sorted array.
        2. Increment the index of the sorted array.
    4. Swap the element at the index of the unsorted array with the element at the index of the minimum element.
    5. Increment the index of the unsorted array.
3. Return the array.
4. Return the result of calling selection sort on the array.
5. Return the sorted array.

### Pseudocode (Selection Sort)

```python
def selection_sort(array):
    unsorted_index = 0
    while unsorted_index < len(array) - 1:
        min_index = unsorted_index
        sorted_index = unsorted_index + 1
        while sorted_index < len(array):
            if array[sorted_index] < array[min_index]:
                min_index = sorted_index
            sorted_index += 1
        array[unsorted_index], array[min_index] = array[min_index], array[unsorted_index]
        unsorted_index += 1
    return array
```

### Example (Selection Sort)

```python
>>> selection_sort([5, 4, 3, 2, 1])
[1, 2, 3, 4, 5]
```

### Complexity (Selection Sort)

| Name | Best | Average | Worst | Memory | Stable | Comments | Data Structure |
| ---- | ---- | ------- | ----- | ------ | ------ | -------- | -------------- |
| Selection Sort | O(n^2) | O(n^2) | O(n^2) | O(1) | No | - | Array |

### References (Selection Sort)

- [Wikipedia](https://en.wikipedia.org/wiki/Selection_sort) - Selection sort algorithm
- [GeeksforGeeks](https://www.geeksforgeeks.org/selection-sort/) - Selection Sort

---

## Merge Sort

Merge sort is a sorting algorithm that sorts an array by repeatedly dividing the array into two halves, sorting the two halves, and merging them together. This type of sorting algorithm is very efficient, with time complexity of O(n log n). However, it requires additional memory space to store the two halves of the array. Merge sort is a divide and conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 

### Algorithm (Merge Sort)

1. If the length of the array is 1, return the array.
2. Set the middle index to the length of the array divided by 2, rounded down.
3. Set the left array to the result of calling merge sort on the left half of the array.
4. Set the right array to the result of calling merge sort on the right half of the array.
5. Set the index of the left array to 0.
6. Set the index of the right array to 0.
7. Set the index of the merged array to 0.
8. While the index of the left array is less than the length of the left array and the index of the right array is less than the length of the right array:
    1. If the element at the index of the left array is less than the element at the index of the right array:
        1. Set the element at the index of the merged array to the element at the index of the left array.
        2. Increment the index of the left array.
    2. Else:
        1. Set the element at the index of the merged array to the element at the index of the right array.
        2. Increment the index of the right array.
    3. Increment the index of the merged array.
9. While the index of the left array is less than the length of the left array:
    1. Set the element at the index of the merged array to the element at the index of the left array.
    2. Increment the index of the left array.
    3. Increment the index of the merged array.
10. While the index of the right array is less than the length of the right array: 
    1. Set the element at the index of the merged array to the element at the index of the right array.
    2. Increment the index of the right array.
    3. Increment the index of the merged array.
11. Return the merged array.
12. Return the result of calling merge sort on the array.
13. Return the sorted array.

### Pseudocode (Merge Sort)

```python
def merge_sort(array):
    if len(array) == 1:
        return array
    middle_index = len(array) // 2
    left_array = merge_sort(array[:middle_index])
    right_array = merge_sort(array[middle_index:])
    left_index = 0
    right_index = 0
    merged_index = 0
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            array[merged_index] = left_array[left_index]
            left_index += 1
        else:
            array[merged_index] = right_array[right_index]
            right_index += 1
        merged_index += 1
    while left_index < len(left_array):
        array[merged_index] = left_array[left_index]
        left_index += 1
        merged_index += 1
    while right_index < len(right_array):
        array[merged_index] = right_array[right_index]
        right_index += 1
        merged_index += 1
    return array
```

### Example (Merge Sort)

```python
>>> merge_sort([5, 4, 3, 2, 1])
[1, 2, 3, 4, 5]
```

### Complexity (Merge Sort)

| Name | Best | Average | Worst | Memory | Stable | Comments | Data Structure |
| ---- | ---- | ------- | ----- | ------ | ------ | -------- | -------------- |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | - | Array |

### References (Merge Sort)

- [Wikipedia](https://en.wikipedia.org/wiki/Merge_sort) - Merge sort algorithm
- [GeeksforGeeks](https://www.geeksforgeeks.org/merge-sort/) - Merge Sort
