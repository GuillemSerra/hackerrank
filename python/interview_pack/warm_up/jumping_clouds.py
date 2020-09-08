from typing import List


def jumping_on_clouds(clouds: List[int]) -> int:
    """
    Given list [0, 1, 0, 0, 0, 1, 0], find shortest path thorugh 0's. You can always get to the end.
    """
    HAPPY_CLOUD = 0

    max_position = len(clouds) - 1
    position = 0
    counter_jumps = 0

    while position < max_position:
        if (position + 2) <= max_position and clouds[position + 2] == HAPPY_CLOUD:
            position += 2
        elif clouds[position + 1] == HAPPY_CLOUD:
            position += 1

        counter_jumps += 1

    return counter_jumps


sample_1 = [0, 0, 0, 0, 1, 0]
expected_1 = 3
sample_2 = [0, 0, 1, 0, 0, 1, 0]
expected_2 = 4
sample_3 = [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
expected_3 = 5

assert jumping_on_clouds(sample_1) == expected_1
assert jumping_on_clouds(sample_2) == expected_2
assert jumping_on_clouds(sample_3) == expected_3
