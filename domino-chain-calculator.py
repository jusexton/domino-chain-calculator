from anytree import Node, RenderTree, DoubleStyle
# TODO: Make use of anytree iterators to determine best possible tree paths


class Domino:
    def __init__(self, valueOne, valueTwo=None):
        if valueOne < 0 or valueTwo < 0:
            raise ValueError('Both supplied values must not be negative')

        if not isinstance(valueOne, int) or not isinstance(valueTwo, int):
            raise ValueError('Both supplied values must be integers')

        self.valueOne = valueOne
        self.valueTwo = valueOne if valueTwo is None else valueTwo

    def contains(self, value):
        """
        Return whether one of the domino values is a given value.
        """
        return self.valueOne == value or self.valueTwo == value

    def opposite_of(self, value):
        """
        Given a value, returns the opposite of that value if it exists within the domino instance.
        Otherwise return -1.
        """
        if self.valueOne == value:
            return self.valueTwo
        elif self.valueTwo == value:
            return self.valueOne
        else:
            return -1

    def is_double(self):
        """
        Returns whether the domino instance is a double. (If both domnio values are the same)
        """
        return self.valueOne == self.valueTwo

    def invert(self):
        return Domino(self.valueTwo, self.valueOne)

    def __repr__(self):
        return f'Domino [{self.valueOne} {self.valueTwo}]'

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.valueOne == other.valueOne and self.valueTwo == other.valueTwo

    def __hash__(self):
        return hash(str(self.valueOne) + str(self.valueTwo))


class DominoTree:
    def __init__(self, starting_value):
        self.root_node = Node(starting_value)

    @staticmethod
    def create(dominoes, starting_value):
        tree = DominoTree(starting_value)
        return DominoTree._create(dominoes, starting_value, tree.root_node, tree)

    @staticmethod
    def _create(dominoes, starting_value, parent, tree):
        for domino in dominoes:
            if domino.contains(starting_value):
                new = Node(domino, parent=parent)
                unused = set(filter(lambda d: d != domino, dominoes))
                tree = DominoTree._create(
                    unused, domino.opposite_of(starting_value), new, tree)

        return tree


def main():
    starting_value = 5
    domino_list = load_dominoes('dominoes.txt')

    tree = DominoTree.create(domino_list, starting_value)
    print(RenderTree(tree.root_node, style=DoubleStyle))


def load_dominoes(source):
    """
    Given a file path, returns list of dominoes.
    Ex.
    6,5
    11,4
    5,1
    ...
    """
    with open(source) as file:
        lines = file.read().splitlines()
        split_lines = map(lambda line: line.split(','), lines)
        dominoes = map(lambda values: Domino(
            int(values[0]), int(values[1])), split_lines)
        return list(dominoes)


if __name__ == "__main__":
    main()
