from anytree import Node


def domino_count(n: int) -> int:
    u"""
    Calculates how many total dominoes are in a set given the max double
    """
    if n < 0:
        raise ValueError('does not make sense for given value to be negative')

    return ((n ** 2) + (n * 3) + 2) / 2


def sum_domino_node(node: Node) -> int:
    u"""
    Given a node with its name being a Domino, sums the node's domino value with its ancestors domino values.

    [5 5]/[2 3] -> 15
    """
    return sum([node.name.total_value() for node in node.path])
