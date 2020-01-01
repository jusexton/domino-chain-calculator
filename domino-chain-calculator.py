from argparse import ArgumentParser, RawTextHelpFormatter

from anytree import DoubleStyle, RenderTree

from dominoes import DominoData, DominoTree

description_path = "description.txt"


def get_description() -> str:
    with open(description_path) as file:
        return file.read()


def build_argument_parser():
    description = get_description()

    parser = ArgumentParser(
        description=description, formatter_class=RawTextHelpFormatter)

    parser.add_argument('-s', '--source', action='store', required=True,
                        help='the source json file that will be used as domino data')

    # parser.add_argument('-v', '--verbose', action='store_true',
    #                     help='Shows all possible combinations of dominoes, not just the best route')

    return parser


if __name__ == '__main__':
    # TODO: Make use of anytree iterators to determine best possible tree paths
    # TODO: By default, should instead only display the best possible domino chain
    # TODO: Add -v --verbose option to display all possible combinations with best path color coordinated.
    # TODO: Add ability to build domino list from picture of dominoes (ambitious)

    argument_parser = build_argument_parser()
    args = argument_parser.parse_args()

    domino_data = DominoData.read(args.source)

    tree = DominoTree.create(domino_data)
    print(RenderTree(tree.root_node, style=DoubleStyle))
