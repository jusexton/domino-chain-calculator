from __future__ import annotations

from typing import Iterable

from anytree import Node

from dominoes import Domino, DominoData


# TODO: Should be refactored. Class design makes no sense.
class DominoTree(object):
    def __init__(self, starting_value: int):
        starting_domino = Domino(starting_value)
        self.root_node = Node(starting_domino)

        self.best_route = None

    @staticmethod
    def create(domino_data: DominoData, unique: bool = True) -> DominoTree:
        domino_list = domino_data.domino_list
        starting_value = domino_data.starting_value

        if unique and len(set(domino_list)) != len(domino_list):
            raise ValueError('All given dominoes must be unique')

        tree = DominoTree(starting_value)
        return DominoTree._create(domino_list, starting_value, tree.root_node, tree)

    @staticmethod
    def _create(dominoes: Iterable[Domino], starting_value: int, parent: Node, tree: DominoTree) -> DominoTree:
        for domino in dominoes:
            if domino.contains(starting_value):
                new = Node(domino, parent=parent)
                unused = set(filter(lambda d: d != domino, dominoes))
                tree = DominoTree._create(
                    unused, domino.opposite_of(starting_value), new, tree)

        return tree
