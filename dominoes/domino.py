import json


class Domino(object):
    def __init__(self, valueOne, valueTwo=None):
        u"""
        Simple domino instance representing a single domino.

        If no second value is given, the domino is assumed to be a double and the given value will represent both
        of the dominoes values
        """
        if valueTwo is None:
            valueTwo = valueOne

        if valueOne < 0 or valueTwo < 0:
            raise ValueError('Both supplied values must not be negative')

        self.valueOne = valueOne
        self.valueTwo = valueTwo

    def contains(self, value):
        u"""
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
        u"""
        Returns whether the domino instance is a double. (If both domnio values are the same)
        """
        return self.valueOne == self.valueTwo

    def invert(self):
        u"""
        Returns a new domino with inverted values
        """
        return Domino(self.valueTwo, self.valueOne)

    def __repr__(self):
        return f'[{self.valueOne} {self.valueTwo}]'

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.valueOne == other.valueOne and self.valueTwo == other.valueTwo

    def __hash__(self):
        return hash(str(self.valueOne) + str(self.valueTwo))


class DominoData(object):
    STARTING_VALUE_NAME = 'startingValue'
    DOMINO_VALUE_ONE_NAME = 'valueOne'
    DOMINO_VALUE_TWO_NAME = 'valueTwo'
    DOMINO_LIST_NAME = 'dominoes'

    def __init__(self, starting_value, domino_list):
        self.starting_value = starting_value
        self.domino_list = domino_list

    @staticmethod
    def read(source):
        with open(source) as file:
            data = json.load(file)
            starting_value = data[DominoData.STARTING_VALUE_NAME]
            domino_list = [Domino(domino_values[DominoData.DOMINO_VALUE_ONE_NAME], domino_values[DominoData.DOMINO_VALUE_TWO_NAME])
                           for domino_values in data[DominoData.DOMINO_LIST_NAME]]

        return DominoData(starting_value, domino_list)


def create_reandom_domino(valueOneRange, valueTwoRange):
    import random
    valueOne = random.randint(valueOneRange[0], valueOneRange[1])
    valueTwo = random.randint(valueTwoRange[0], valueTwoRange[1])
    return Domino(valueOne, valueTwo)
