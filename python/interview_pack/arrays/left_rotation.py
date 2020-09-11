from typing import List


def rotate_left(array: List[int], rotations: int) -> List[int]:
    """
    Circular rotate left where rotations < len(array)
    """
    tail = array[:rotations]
    head = array[rotations:]

    return head + tail


assert rotate_left([1, 2, 3, 4, 5], 4) == [5, 1, 2, 3, 4]
assert rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
