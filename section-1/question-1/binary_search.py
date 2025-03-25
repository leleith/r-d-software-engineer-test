"""
Q: Implement a function in Python that performs a binary search
on a sorted list and returns the index of the target element.
If the element is not found, return -1
"""

from typing import Literal


def check_sorting_order(
        l: list[int]
) -> Literal["ascending", "descending", "unsorted"]:
    """
    This function checks the order of sorting of a list of integers

    Return:
        a string containing the result
    """
    # checking if the list is sorted in ascending order
    if all(l[i] <= l[i + 1] for i in range(len(l) - 1)):
        return "ascending"
    # checking if the list is sorted in ascending order
    elif all(l[i] >= l[i + 1] for i in range(len(l) - 1)):
        return "descending"
    else:
        return "unsorted"


def binary_search(
        elements: list[int],
        value: int
) -> int:
    # check if the list is sorted, otherwise sort it
    if check_sorting_order(elements) != "ascending":
        elements = sorted(elements)
    
    # defining control variables
    left: int = 0
    right: int = len(elements) - 1

    while left <= right:
        middle: int = (left + right) // 2

        # Target found at the middle index
        if elements[middle] == value:
            return middle
        # Target is in the right half
        elif elements[middle] < value:
            left = middle + 1
        # Target is in the left half
        else:
            right = middle - 1

    return -1


if __name__ == "__main__":
    sorted_list = [12, 2, 8, 5, 16, 91, 38, 56, 72, 23]

    assert binary_search(sorted_list, 56) == 7
    assert binary_search(sorted_list, 91) == 9
    assert binary_search(sorted_list, 5) == 1
    assert binary_search(sorted_list, 50) == -1
    assert binary_search(sorted_list, 2) == 0

    print("All tests passed!")
