from collections import Counter


def repeated_string(string: str, n: int) -> int:
    """
    It should return an integer representing the number of occurrences of 'a' in the prefix
    of length  in the infinitely repeating string.
    """
    number_of_a = Counter(string)['a']
    remaining_letters = n % len(string)
    remaining_a = Counter(string[:remaining_letters])['a']

    number_of_a *= int(n / len(string))
    number_of_a += remaining_a

    return number_of_a


sample_string_1 = 'abcac'
sample_n_1 = 10
assert repeated_string(sample_string_1, sample_n_1) == 4
sample_string_2 = 'aba'
sample_n_2 = 10
assert repeated_string(sample_string_2, sample_n_2) == 7
sample_string_3 = 'a'
sample_n_3 = 1000000000000
assert repeated_string(sample_string_3, sample_n_3) == 1000000000000
