from anytree import Node
from dominoes import Domino


# TODO: Should be refactored. Class design makes no sense.
class DominoTree(object):
    def __init__(self, starting_value):
        starting_domino = Domino(starting_value)
        self.root_node = Node(starting_domino)

    @staticmethod
    def create(domino_data, unique=True):
        domino_list = domino_data.domino_list
        starting_value = domino_data.starting_value

        if unique and len(set(domino_list)) != len(domino_list):
            raise ValueError('All given dominoes must be unique')

        tree = DominoTree(starting_value)
        return DominoTree._create(domino_list, starting_value, tree.root_node, tree)

    @staticmethod
    def _create(dominoes, starting_value, parent, tree):
        for domino in dominoes:
            if domino.contains(starting_value):
                new = Node(domino, parent=parent)
                unused = set(filter(lambda d: d != domino, dominoes))
                tree = DominoTree._create(
                    unused, domino.opposite_of(starting_value), new, tree)

        return tree
