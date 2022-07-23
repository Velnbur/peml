import sys
from typing import List

from parser.parsing import tokenize
from parser.ast.contract import Contract


def main(argv: List[str]):
    path = argv[0]

    tokens = []
    with open(path, "r") as file:
        tokens = tokenize(file.read())

    for line in tokens:
        for token in line:
            print(token._type, end=" ")
        print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <input_file>")
        sys.exit(1)

    main(sys.argv[1:])
