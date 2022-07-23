"""
This module contains the parsing functions for the parser.
"""
from typing import List

from parser.ast.tokens import Token, Type as TokenType
from parser.ast.expressions import Expression


def parse_line(line: List[Token]) -> Expression:
    """
    This function parses a line of tokens.
    """
    return Expression()


def _organize(buff: str) -> str:
    """
    This functions organizes buffer with the code so it will be easier to
    tokenize and parse.

    1. Removes all comments.
    2. Strip every line from whitespaces and tabs.
    2. If line ends with ',\n' replace it with ','.
    3. Add spaces around parentheses, commas.

    Remove all comments.

    Add spaces around parentheses, commas and operators.
    This is done by replacing the following symbols with the following
    symbols with a space in front of them:
      (  ) ,
    """

    return (
        _replace_commas(_remove_comments(buff))
        .replace("\t", " \t ")
        .replace("(", " ( ")
        .replace(")", " ) ")
        .replace(",", " , ")
    )


COMMENT_SYMBOL = "#"


def _remove_comments(buff: str) -> str:
    """
    This functions removes all comments from the buffer.
    """
    return "\n".join(
        [
            line
            for line in [line.split(COMMENT_SYMBOL)[0] for line in buff.split("\n")]
            if line.strip()
        ]
    )


def _replace_commas(buff: str) -> str:
    """
    If on the end if the line there is a ','
    the next line will be concatenated to the current line.
    """
    lines = buff.split("\n")
    res = []

    lines_iter = iter(lines)
    for line in lines_iter:
        if line.endswith(","):
            res.append(line + next(lines_iter))
            continue
        res.append(line)

    return "\n".join(res)


def tokenize(buff: str) -> List[List[Token]]:
    """
    This function tokenizes the buffer.
    """
    buff = _organize(buff)
    return [_tokenize_line(line) for line in buff.split("\n")]


def _tokenize_line(line: str) -> List[Token]:
    """
    This function tokenizes a line.
    """
    res = []
    for word in line.split(" "):
        if word == "":
            continue

        try:
            res.append(Token(TokenType(word), word))
            continue
        except ValueError:
            pass
        if word.isdigit():
            res.append(Token(TokenType.INT, word))
        elif word.startswith('"') and word.endswith('"'):
            res.append(Token(TokenType.STRING, word))
        elif word.isidentifier():
            res.append(Token(TokenType.IDENTIFIER, word))
        else:
            raise ValueError(f"Unknown token: {word}")

    return res
