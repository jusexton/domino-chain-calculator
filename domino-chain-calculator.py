from argparse import ArgumentParser, RawTextHelpFormatter

from anytree import DoubleStyle, RenderTree

from dominoes import DominoData, DominoTree


def build_argument_parser():
    with open('description.txt') as file:
        description = file.read()

    parser = ArgumentParser(
        description=description, formatter_class=RawTextHelpFormatter)

    parser.add_argument('-s', '--source', action='store', required=True,
                        help='the source json file that will be used as domino data')

    # parser.add_argument('-v', '--verbose', action='store_true',
    #                     help='Shows all possible combinations of dominoes, not just the best route')

    return parser


def main():
    # TODO: Make use of anytree iterators to determine best possible tree paths
    # TODO: Add ability to build domino list from picture of dominoes (ambitioues)
    parser = build_argument_parser()
    args = parser.parse_args()

    data = DominoData.read(args.source)

    tree = DominoTree.create(data)
    print(RenderTree(tree.root_node, style=DoubleStyle))


if __name__ == "__main__":
    main()
