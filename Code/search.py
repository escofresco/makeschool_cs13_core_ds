#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index >= len(array):
        return
    if array[index] == item:
        return index
    return linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    lo = 0
    hi = len(array) - 1

    while lo <= hi:
        mid = (hi + lo) // 2

        if array[mid] == item:
            return mid

        if array[mid] < item:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def binary_search_recursive(array, item, left=0, right=None):
    
    if right is None:
        right = len(array) - 1

    if left > right:
        return None
    mid = (left + right) // 2

    if array[mid] == item:
        return mid

    if array[mid] < item:
        return binary_search_recursive(array, item, mid + 1, right)
    return binary_search_recursive(array, item, left, mid - 1)
