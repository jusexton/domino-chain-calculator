from __future__ import annotations

import random
from typing import Tuple, List

from marshmallow import Schema, fields, post_load


class Domino:
    def __init__(self, value_one: int, value_two: int = None):
        u"""
        Simple domino instance representing a single domino.

        If no second value is given, the domino is assumed to be a double and the given value will represent both
        of the dominoes values
        """
        if value_two is None:
            value_two = value_one

        self.value_one = value_one
        self.value_two = value_two

    @property
    def value_one(self):
        return self._value_one

    @value_one.setter
    def value_one(self, value_one):
        u"""
        Sets given value one as this instances value two.
        Does not accept negative values
        """
        if value_one < 0:
            raise ValueError('value cannot be negative')

        self._value_one = value_one

    @property
    def value_two(self):
        return self._value_two

    @value_two.setter
    def value_two(self, value_two):
        u"""
        Sets given value two as this instances value two.
        Does not accept negative values
        """
        if value_two < 0:
            raise ValueError('value cannot be negative')

        self._value_two = value_two

    def contains(self, value: int) -> bool:
        u"""
        Return whether one of the domino values is a given value.
        """
        return self.value_one == value or self.value_two == value

    def opposite_of(self, value: int) -> int:
        """
        Given a value, returns the opposite of that value if it exists within the domino instance.
        Otherwise return -1.
        """
        if self.value_one == value:
            return self.value_two
        elif self.value_two == value:
            return self.value_one
        else:
            return -1

    def is_double(self) -> bool:
        u"""
        Returns whether the domino instance is a double. (If both domino values are the same)
        """
        return self.value_one == self.value_two

    def invert(self) -> Domino:
        u"""
        Returns a new domino with inverted values
        """
        return Domino(self.value_two, self.value_one)

    def total_value(self):
        return self.value_one + self.value_two

    @staticmethod
    def random(value_one_range: Tuple[int, int] = (1, 12), value_two_range: Tuple[int, int] = (1, 12)) -> Domino:
        u"""
        Creates a domino with random values
        """
        value_one = random.randint(value_one_range[0], value_one_range[1])
        value_two = random.randint(value_two_range[0], value_two_range[1])
        return Domino(value_one, value_two)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(value_one={self.value_one}, value_two={self.value_two})'

    def __str__(self) -> str:
        return f'[{self.value_one} {self.value_two}]'

    def __iter__(self):
        yield from [self.value_one, self.value_two]

    def __eq__(self, other: Domino) -> bool:
        return self.__class__ == other.__class__ and \
               self.value_one == other.value_one and \
               self.value_two == other.value_two

    def __hash__(self) -> int:
        return hash(str(self.value_one) + str(self.value_two))

    def __add__(self, other: Domino) -> Domino:
        return Domino(self.value_one + other.value_one, self.value_two + other.value_two)

    def __gt__(self, other: Domino) -> bool:
        return self.total_value() > other.total_value()

    def __lt__(self, other: Domino) -> bool:
        return self.total_value() < other.total_value()


class DominoData:
    def __init__(self, starting_value: int, domino_list: List[Domino]):
        u"""
        Creates new domino data instance.
        Instance is used to encapsulate information regarding a domino game.
        """
        self.starting_value = starting_value
        self.domino_list = domino_list

    def __iter__(self):
        yield from [self.starting_value, self.domino_list]


class DominoSchema(Schema):
    value_one = fields.Integer()
    value_two = fields.Integer()

    @post_load
    def to_domino(self, data, **kwargs):
        return Domino(**data)


class DominoDataSchema(Schema):
    starting_value = fields.Integer()
    domino_list = fields.List(fields.Nested(DominoSchema))

    @post_load
    def to_domino_data(self, data, **kwargs):
        return DominoData(**data)
