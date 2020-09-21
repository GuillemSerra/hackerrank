from typing import List


def min_swaps(array: List[int]) -> int:
    """
    Given an unordered list of consecutive integers, return the minimum number of swaps to order it
    in ASC order.
    """
    n_swaps = 0
    index = 0

    while index < len(array):
        next_position = index + 1
        is_correct_position = array[index] == next_position
        if is_correct_position:
            index += 1
            continue

        counter = index
        while array[counter] != index + 1:
            counter += 1

        array[index], array[counter] = array[counter], array[index]
        n_swaps += 1
        index += 1

    return n_swaps


assert min_swaps([2, 3, 4, 1, 5]) == 3
assert min_swaps([1, 3, 5, 2, 4, 6, 7]) == 3
assert min_swaps([4, 3, 1, 2]) == 3
assert min_swaps([7, 1, 3, 2, 4, 5, 6]) == 5
