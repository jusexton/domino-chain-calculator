from argparse import ArgumentParser, RawTextHelpFormatter
import json

from anytree import DoubleStyle, RenderTree

import dominoes
from dominoes.types import Domino, DominoData

description_path = "assets/description.txt"


def read_description() -> str:
    with open(description_path) as file:
        return file.read()


def read_domino_data(source: str) -> DominoData:
    with open(source) as file:
        data = json.load(file)
        dominoes = [Domino(**d) for d in data["dominoes"]]
        return DominoData(starting_value=data["starting_value"], dominoes=dominoes)


def build_argument_parser():
    description = read_description()

    parser = ArgumentParser(
        description=description, formatter_class=RawTextHelpFormatter
    )

    parser.add_argument(
        "-s",
        "--source",
        action="store",
        required=True,
        help="the source json file that will be used as domino data",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="displays all possible routes instead of just the most optimized",
    )

    parser.add_argument(
        "-i",
        "--include-sum",
        action="store_true",
        help="displays a summation of a node and its ancestors values alongside the node representation",
    )

    return parser


if __name__ == "__main__":
    # TODO: Add ability to build domino list from picture of dominoes (ambitious)

    argument_parser = build_argument_parser()
    args = argument_parser.parse_args()

    domino_data = read_domino_data(args.source)

    options = {"include_sum": args.include_sum, **domino_data.model_dump()}
    root_node = dominoes.all(**options) if args.verbose else dominoes.best(**options)

    print(RenderTree(root_node, style=DoubleStyle))
