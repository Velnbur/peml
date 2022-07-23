"""
This is a moduel for all the tokens used in the parser.
"""

import enum


@enum.unique
class Type(enum.Enum):
    # Keywords
    CONTRACT = "contract"
    FUNCTION = "func"
    FIELD = "field"
    LET = "let"
    RETURN = "return"
    IF = "if"
    ELSE = "else"
    WHILE = "while"
    THEN = "then"
    ARROW = "=>"
    IDENTATION = "\t"
    END = "end"

    # Literals
    TRUE = "true"
    FALSE = "false"

    # Operators
    ASSIGN = ":="
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    MODULO = "%"
    EQ = "="
    NEQ = "!="
    LT = "<"
    GT = ">"
    LTE = "<="
    GTE = ">="
    AND = "and"
    OR = "or"
    NOT = "not"

    # Delimiters
    LPAREN = "("
    RPAREN = ")"
    COMMA = ","

    # Other
    IDENTIFIER = "identifier"
    INT = "int"
    STRING = "string"


class Token:
    """
    This class represents a token
    """

    _type: Type
    value: str

    def __init__(self, _type: Type, value: str):
        self._type = _type
        self.value = value

    def __str__(self):
        return f"type: {self._type}, value: {self.value}"

    def __repr__(self):
        return self.__str__()
