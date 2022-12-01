# binary search algorithm

class BinarySearch:

    # docstring
    """Binary search algorithm
    Time complexity: O(logn)
    Space complexity: O(1)

    Parameters
    ----------
    arr: list
        a sorted array or unsorted array (if not sorted, sort it first)
    target: int
        the target value

    Returns
    -------
    int
        the index of the target value

    Examples
    --------
    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> binary_search(arr, 5)
    4
    >>> binary_search(arr, 10)
    -1
    """

    def __init__(self, arr):
        self.arr = arr

    # if arr in not sorted, sort it
    def sort(self):
        print(f"Array before sorting: {self.arr}")
        self.arr.sort()

    # generate a random array
    @staticmethod
    def generate_array(n):
        import random
        return [random.randint(0, 100) for _ in range(n)]

    # type 1: iterative
    def binary_search(self, target):
        left, right = 0, len(self.arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # type 2: recursive
    def binary_search_recursive(self, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if self.arr[mid] == target:
            return mid
        elif self.arr[mid] < target:
            return self.binary_search_recursive(target, mid + 1, right)
        else:
            return self.binary_search_recursive(target, left, mid - 1)

    # type 3: modified binary search
    def modified_binary_search(self, target):
        left, right = 0, len(self.arr) - 1
        while left < right:
            mid = (left + right) // 2
            if self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        if self.arr[left] == target:
            return left
        else:
            return -1

    # calculate the time complexity
    def time_complexity(self, stmt, setup):
        from timeit import timeit
        return timeit(stmt=stmt, setup=setup, number=10000)

    # print docstring

    def __repr__(self):
        return f"{self.__doc__}"


if __name__ == '__main__':

    # generate a random array
    arr = BinarySearch.generate_array(100)
    bs = BinarySearch(arr)
    print(bs)
    bs.sort()
    key = int(input("Enter the key: "))
    print(f"Index of {key} is {bs.binary_search(key)} (iterative)")
    print(
        f"Index of {key} is {bs.binary_search_recursive(key, 0, len(arr) - 1)} (recursive)")
    print(f"Index of {key} is {bs.modified_binary_search(key)} (modified)")

    # calculate time complexity
    setup = "from __main__ import bs, key, arr"
    stmt = "bs.binary_search(key)"
    print(f"Time complexity: {bs.time_complexity(stmt, setup)} (iterative)")
    stmt = "bs.binary_search_recursive(key, 0, len(arr) - 1)"
    print(f"Time complexity: {bs.time_complexity(stmt, setup)} (recursive)")
    stmt = "bs.modified_binary_search(key)"
    print(f"Time complexity: {bs.time_complexity(stmt, setup)} (modified)")
