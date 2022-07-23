"""
This module declares a class for the AST of a contract.
"""
from __future__ import annotations
from typing import List

from parser.ast.function import Function
from parser.ast.field import Field
from parser.ast.tokens import Token, Type as TokenType
from parser.ast.expressions import Variable


class Contract:
    """
    This class represents the AST of a contract.
    """

    name: str
    functions: List[Function]
    fields: List[Field]

    variables: List[Variable]

    def __init__(self, name: str, functions: List[Function], fields: List[Field]):
        self.name = name
        self.functions = functions
        self.fields = fields

        self.variables = [Variable(field.name, field._type) for field in self.fields]

    @classmethod
    def from_tokens(cls, lines: List[List[Token]]) -> Contract:
        """
        This method creates a contract from a list of tokens.

        Example:
            contract Foo
                ...
            end
        """
        name = lines[0][1].value
        functions = []
        fields = []
        lines = lines[1 : len(lines) - 1]
        lines_iter = enumerate(lines)

        for i, tokens in lines_iter:
            if (
                tokens[0]._type == TokenType.IDENTATION
                and tokens[1]._type == TokenType.FUNCTION
            ):
                end_index = cls._find_func_end(lines[i + 1 :])
                functions.append(Function.from_tokens(lines[i : end_index + i + 1]))

                # Skip already parsed lines
                for i in range(end_index):
                    lines_iter.__next__()

            elif (
                tokens[0]._type == TokenType.IDENTATION
                and tokens[1]._type == TokenType.FIELD
            ):
                fields.append(Field.from_tokens(tokens))
        return cls(name, functions, fields)

    @staticmethod
    def _find_func_end(lines: List[List[Token]]) -> int:
        """
        This method finds the nearest end of function
        """
        for i, line in enumerate(lines):
            if line[0]._type == TokenType.IDENTATION and line[1]._type == TokenType.END:
                return i
        raise Exception("No end found.")

    def __str__(self) -> str:
        """
        This method returns a string representation of the contract.
        """
        return f"contract {self.name}\n{''.join(str(f) for f in self.functions)}\n{''.join(str(f) for f in self.fields)}\nend"
