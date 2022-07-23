"""
This is module for the Field class.

"Field" is a class for the field of a contract.
"""
from __future__ import annotations

import enum
from typing import List

from parser.ast.tokens import Token, Type as TokenType
from parser.ast import types


@enum.unique
class AccessType(enum.Enum):
    """
    This is an enum for the access type of a field.
    """

    PRIVATE = enum.auto()
    PUBLIC = enum.auto()


class Field:
    """
    This is a class for the field of a contract.
    """

    name: str
    access: AccessType
    _type: types.Types

    def __init__(
        self, name: str, _type: types.Types, access: AccessType = AccessType.PRIVATE
    ):
        """
        This is the constructor for the Field class.
        """

        self.name = name
        self._type = _type
        self.access = access

    @classmethod
    def from_tokens(cls, toks: List[Token]) -> Field:
        """
        This is a class method for the Field class.

        Example:
            field count u256
        """
        if len(toks) < 3 or len(toks) > 4:
            raise ValueError("invalid field")

        if (
            toks[0]._type != TokenType.IDENTATION
            or toks[1]._type != TokenType.FIELD
            or toks[2]._type != TokenType.IDENTIFIER
            or toks[3]._type != TokenType.IDENTIFIER
        ):
            raise ValueError(f"invalid field {toks}")

        return cls(toks[2].value, types.Types[toks[3].value])

    def __str__(self) -> str:
        return f"field {self.access} {self.name} {self._type}"
