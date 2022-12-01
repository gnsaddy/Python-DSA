# linear search algorithm

class LinearSearch:

    # docstring
    """Linear search algorithm
    Time complexity: O(n)
    Space complexity: O(1)

    Parameters
    ----------
    arr: list
        an unsorted array
    target: int
        the target value

    Returns
    -------
    int
        the index of the target value

    Examples
    --------
    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> linear_search(arr, 5)
    4
    >>> linear_search(arr, 10)
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
    def linear_search(self, target):
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                return i
        return -1

    # type 2: recursive
    def linear_search_recursive(self, target, i):
        if i >= len(self.arr):
            return -1
        if self.arr[i] == target:
            return i
        return self.linear_search_recursive(target, i + 1)

    # type 3: modified linear search
    def modified_linear_search(self, target):
        i = 0
        while i < len(self.arr):
            if self.arr[i] == target:
                return i
            i += 1
        return -1

    # type 4: sentinel linear search
    def sentinel_linear_search(self, target):
        self.arr.append(target)
        i = 0
        while self.arr[i] != target:
            i += 1
        self.arr.pop()
        return i if i < len(self.arr) else -1

    # calculate the time complexity
    def time_complexity(self, stmt, setup):
        from timeit import timeit
        return timeit(stmt, setup, number=1000)

    def __repr__(self) -> str:
        return f"{self.__doc__}"


if __name__ == "__main__":
    arr = LinearSearch.generate_array(100)
    ls = LinearSearch(arr)
    print(ls)
    ls.sort()
    key = int(input("Enter the key: "))
    print(f"Index of {key} is {ls.linear_search(key)} (iterative)")
    print(
        f"Index of {key} is {ls.linear_search_recursive(key, 0)} (recursive)")
    print(f"Index of {key} is {ls.modified_linear_search(key)} (modified)")
    print(f"Index of {key} is {ls.sentinel_linear_search(key)} (sentinel)")

    # calculate the time complexity
    setup = "from __main__ import ls, arr, key"
    stmt = "ls.linear_search(key)"
    print(
        f"Time complexity of linear search (iterative): {ls.time_complexity(stmt, setup)}")
    stmt = "ls.linear_search_recursive(key, 0)"
    print(
        f"Time complexity of linear search (recursive): {ls.time_complexity(stmt, setup)}")
    stmt = "ls.modified_linear_search(key)"
    print(
        f"Time complexity of linear search (modified): {ls.time_complexity(stmt, setup)}")
    stmt = "ls.sentinel_linear_search(key)"
    print(
        f"Time complexity of linear search (sentinel): {ls.time_complexity(stmt, setup)}")
