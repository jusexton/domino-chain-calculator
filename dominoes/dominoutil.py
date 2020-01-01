def domino_count(n: int) -> int:
    u"""
    Utility method for determining how many total dominoes are in a set given the max double

    :param n: The max double
    :return: The number of dominoes in the set
    """
    if n < 0:
        raise ValueError('does not make sense for given value to be negative')

    return ((n ** 2) + (n * 3) + 2) / 2
