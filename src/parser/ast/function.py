"""
This module contains the Function class for the AST.
"""

from __future__ import annotations
from typing import List, Tuple

from parser.ast.types import Types
from parser.ast.expressions import Expression, Variable
from parser.ast import tokens


class Function:
    """
    This class represents a function in the AST.
    """

    name: str
    args: List[Tuple[str, Types]]
    return_type: Types
    body: List[Expression]

    variables: List[Variable]

    def __init__(
        self,
        name: str,
        args: List[Tuple[str, Types]],
        body: List[Expression],
        return_type: Types,
    ):
        self.name = name
        self.args = args
        self.body = body
        self.return_type = return_type

        self.variables = [Variable(arg[0], arg[1]) for arg in args]

    @classmethod
    def from_tokens(cls, lines: List[List[tokens.Token]]) -> Function:
        """
        This method parses a function from a list of tokens.
        """
        name, args, return_type = cls._parse_title(lines[0])

        for line in lines[1 : len(lines) - 1]:
            pass

        return cls(name, args, [], return_type)

    @staticmethod
    def _parse_title(
        title: List[tokens.Token],
    ) -> Tuple[str, List[Tuple[str, Types]], Types]:
        """
        This method parses the title of a function and returns the name, arguments and return type.

        Example of gunction title:
            func foo(a u256, b u256) => float
        """
        if (
            title[0]._type != tokens.Type.IDENTATION
            or title[1]._type != tokens.Type.FUNCTION
            or title[2]._type != tokens.Type.IDENTIFIER
            or title[3]._type != tokens.Type.LPAREN
            or title[-3]._type != tokens.Type.RPAREN
            or title[-2]._type != tokens.Type.ARROW
            or title[-1]._type != tokens.Type.IDENTIFIER
        ):
            raise ValueError(f"Invalid function title {title}")
        return (
            title[2].value,
            [
                (title[i].value, Types(title[i + 1].value))
                for i in range(3, len(title) - 2, 3)
                if title[i]._type == tokens.Type.IDENTIFIER
                and title[i + 1]._type == tokens.Type.IDENTIFIER
            ],
            Types[title[-1].value],
        )

    def __str__(self) -> str:
        return f"func {self.name}({[arg for arg in self.args]}) => {self.return_type} ... end"
