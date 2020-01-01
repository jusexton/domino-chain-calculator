from random import randint
from unittest import TestCase

from parameterized import parameterized

from dominoes.dominoutil import domino_count


class TestDominoUtil(TestCase):
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
