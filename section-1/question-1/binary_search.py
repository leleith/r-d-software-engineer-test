"""
Q: Implement a function in Python that performs a binary search
on a sorted list and returns the index of the target element.
If the element is not found, return -1
"""

from typing import Literal
import argparse


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
    
    print(f"List of values: {elements}. Value to search: {value}")
    
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
    # Taking arguments via terminal
    parser = argparse.ArgumentParser(description='Binary search.')
    parser.add_argument(
        '-l', '--list_of_numbers', 
        type=str, 
        help='The list of numbers (it does not need to be sorted).'
    )
    parser.add_argument(
        '-v', '--values', 
        type=str, 
        help='The value to search in the list. You can pass more than one'
    )
    args = parser.parse_args()

    # Converting the lists' values to integers
    list_of_numbers = [int(n) for n in args.list_of_numbers.split(",")]
    values = [int(v) for v in args.values.split(",")]

    # Printing results
    for value in values:
        index = binary_search(list_of_numbers, value)
        print(f"Index of value {value}: {index}\n")
