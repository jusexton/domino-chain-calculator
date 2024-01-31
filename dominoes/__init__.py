from anytree import Node

from dominoes.types import Domino, DoubleDomino


def all(starting_value: int, dominoes: list[Domino], *, include_sum: bool = False):
    """
    Returns all possible routes that can be taken
    """
    starting_domino = DoubleDomino(starting_value)
    root_node = Node(starting_domino)
    return _all_possible(starting_value, dominoes, include_sum, root_node, root_node)


def best(
    starting_value: int, dominoes: list[Domino], *, include_sum: bool = False
) -> Node:
    """
    Returns the best possible route that yields the largest sum
    """
    root_node = all(starting_value, dominoes, include_sum=include_sum)
    domino_sums = [(sum_domino_node(leaf), leaf) for leaf in root_node.leaves]
    return max(domino_sums, key=lambda x: x[0])[1]


def _all_possible(
    starting_value: int,
    dominoes: list[Domino],
    include_sum: bool,
    parent: Node,
    root: Node,
) -> Node:
    for domino in dominoes:
        if domino.contains(starting_value):
            domino_sum_kwarg = (
                {"sum": sum_domino_node(parent) + domino.total_value()}
                if include_sum
                else {}
            )
            new = Node(domino, parent=parent, **domino_sum_kwarg)
            unused = [d for d in dominoes if d != domino]
            root = _all_possible(
                domino.opposite_of(starting_value), unused, include_sum, new, root
            )

    return root


def sum_domino_node(node: Node) -> int:
    """
    Given a node with its name being a Domino, sums the node's domino value with its ancestors domino values.

    [5 5]/[2 3] -> 15
    """
    return sum([node.name.total_value() for node in node.path])
