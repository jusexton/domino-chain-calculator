from dataclasses import dataclass
from typing import Any


@dataclass
class Domino:
    value_one: int
    value_two: int

    def __str__(self):
        return f"{self.value_one}-{self.value_two}"

    def contains(self, value) -> bool:
        return self.value_one == value or self.value_two == value

    def total_value(self) -> int:
        return self.value_one + self.value_two

    def opposite_of(self, value: int) -> int:
        if self.value_one == value:
            return self.value_two
        elif self.value_two == value:
            return self.value_one
        else:
            return -1


class DoubleDomino(Domino):
    def __init__(self, value: int):
        super().__init__(value, value)


@dataclass
class DominoData:
    starting_value: int
    dominoes: list[Domino]

    def model_dump(self) -> Any:
        return {
            "starting_value": self.starting_value,
            "dominoes": self.dominoes,
        }
