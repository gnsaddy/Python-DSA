# Searching algorithms in Python

## List of searching algorithms

- [Binary Search](#binary-search)
- [Linear Search](#linear-search)

---

## Binary Search 

Binary search is a searching algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array. This type of search algorithm is very efficient, with time complexity of O(log n). However, it only works on sorted arrays.

### Algorithm (Binary Search)

1. Set the lower bound to 0 and the upper bound to n-1, where n is the number of elements in the array.
2. If the lower bound is greater than the upper bound, the target is not in the array and the search ends.
3. Set the middle index to the average of the lower and upper bounds, rounded down.
4. If the middle element is the target, the search is done.
5. If the middle element is less than the target, set the lower bound to the middle index + 1 and go to step 2.
6. If the middle element is greater than the target, set the upper bound to the middle index - 1 and go to step 2.
7. If the search ends, the target is not in the array.
8. Return the index of the target.
9. Return -1 if the target is not in the array.

### Pseudocode (Binary Search)

```python
def binary_search(array, target):
    lower_bound = 0
    upper_bound = len(array) - 1
    while lower_bound <= upper_bound:
        middle_index = (lower_bound + upper_bound) // 2
        if array[middle_index] == target:
            return middle_index
        elif array[middle_index] < target:
            lower_bound = middle_index + 1
        else:
            upper_bound = middle_index - 1
    return -1
```

### Example (Binary Search)

```python
>>> binary_search([1, 2, 3, 4, 5], 3)
2
>>> binary_search([1, 2, 3, 4, 5], 6)
-1
```

### Complexity (Binary Search)

| Name | Best | Average | Worst | Memory | Stable | Comments | Data Structure |
| ---- | ---- | ------- | ----- | ------ | ------ | -------- | -------------- |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | No | - | Array |

### References (Binary Search)

- [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm) - Binary search algorithm
- [GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/) - Binary Search

---

## Linear Search

Linear search is a searching algorithm that finds the position of a target value within an array. Linear search sequentially checks each element of the array until a match is found or the whole array has been searched. This type of search algorithm is very inefficient, with time complexity of O(n). However, it works on any type of array.

### Algorithm (Linear Search)

1. Set the index to 0.
2. If the index is equal to the length of the array, the target is not in the array and the search ends.
3. If the element at the index is the target, the search is done.
4. Increment the index and go to step 2.
5. If the search ends, the target is not in the array.
6. Return the index of the target.
7. Return -1 if the target is not in the array.

### Pseudocode (Linear Search)

```python
def linear_search(array, target):
    for index, element in enumerate(array):
        if element == target:
            return index
    return -1
```

### Example (Linear Search)

```python
>>> linear_search([1, 2, 3, 4, 5], 3)
2
>>> linear_search([1, 2, 3, 4, 5], 6)
-1
```

### Complexity (Linear Search)

| Name | Best | Average | Worst | Memory | Stable | Comments | Data Structure |
| ---- | ---- | ------- | ----- | ------ | ------ | -------- | -------------- |
| Linear Search | O(1) | O(n) | O(n) | O(1) | No | - | Array |

### References (Linear Search)

- [Wikipedia](https://en.wikipedia.org/wiki/Linear_search) - Linear search algorithm
- [GeeksforGeeks](https://www.geeksforgeeks.org/linear-search/) - Linear Search
