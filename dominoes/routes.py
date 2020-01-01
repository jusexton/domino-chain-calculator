from __future__ import annotations

from typing import Iterable

from anytree import Node

from dominoes import Domino, DominoData, sum_domino_node


class DominoRoutes:
    def __init__(
            self,
            domino_data: DominoData,
            unique: bool = True,
            include_sum: bool = False):
        self.starting_value, self.domino_list = domino_data

        if unique and len(set(self.domino_list)) != len(self.domino_list):
            raise ValueError('All given dominoes must be unique')

        self.include_sum = include_sum

    def all_possible(self):
        u"""
        Returns all possible routes that can be taken
        """
        starting_domino = Domino(self.starting_value)
        root_node = Node(starting_domino)
        return _all_possible_routes(self.domino_list, self.starting_value, self.include_sum, root_node, root_node)

    def best_possible(self) -> Node:
        u"""
        Returns the best possible route that yields the largest sum
        """
        root_node = self.all_possible()

        leaf_sum_map = {}
        for leaf in root_node.leaves:
            leaf_sum = sum_domino_node(leaf)
            leaf_sum_map[leaf_sum] = leaf

        max_leaf_sum = max(leaf_sum_map.keys())
        return leaf_sum_map[max_leaf_sum]


def _all_possible_routes(domino_list: Iterable[Domino], starting_value: int, include_sum: bool, parent: Node,
                         root: Node) -> Node:
    for domino in domino_list:
        if domino.contains(starting_value):
            domino_sum_kwarg = {'sum': sum_domino_node(parent) + domino.total_value()} if include_sum else {}
            new = Node(domino, parent=parent, **domino_sum_kwarg)
            unused = set(filter(lambda d: d != domino, domino_list))
            root = _all_possible_routes(unused, domino.opposite_of(starting_value), include_sum, new, root)

    return root
