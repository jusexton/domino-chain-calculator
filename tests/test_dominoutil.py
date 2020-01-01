from random import randint
from unittest import TestCase

from anytree import Node
from parameterized import parameterized

from dominoes import domino_count, Domino, sum_domino_node


class TestDominoCount(TestCase):
    @parameterized.expand([
        (1, 0),
        (3, 1),
        (6, 2),
        (10, 3),
        (15, 4),
        (91, 12)
    ])
    def test_should_return_correct_domino_count(self, expected, max_double):
        self.assertEqual(expected, domino_count(max_double))

    def test_should_raise_value_error_when_given_argument_is_not_positive(self):
        with self.assertRaises(ValueError):
            domino_count(-1)

        with self.assertRaises(ValueError):
            random_negative_value = randint(int('-inf'), -1)
            domino_count(random_negative_value)


class TestSumDominoNode(TestCase):
    zero_sum_node = Node(Domino(0))
    five_sum_node = Node(Domino(2, 3), parent=zero_sum_node)
    twenty_sum_node = Node(Domino(10, 5), parent=five_sum_node)

    @parameterized.expand([
        (0, zero_sum_node),
        (5, five_sum_node),
        (20, twenty_sum_node)
    ])
    def test_should_return_correct_sum_of_given_nodes(self, expected, node):
        self.assertEqual(expected, sum_domino_node(node))

    def test_should_raise_attribute_error_when_node_without_domino_name_is_given(self):
        with self.assertRaises(AttributeError):
            sum_domino_node(Node(''))
