"""
This is a module for the AST of the expressions.
"""

from typing import Generic, Optional, TypeVar, List

from parser.ast.types import Types
from parser.ast.tokens import Token, Type as TokenType


class Expression:
    """
    This is the base class for the AST of the expressions.
    """

    def asm(self) -> str:
        """
        This method returns the assembly code for the expression.
        """
        raise NotImplementedError


class Operator(Expression):
    """
    This is the class for the AST of the operators.
    """

    pass


class Unary(Operator):
    """
    This is a base class for all unary expressions
    """

    child: Expression

    def __init__(self, value: Expression):
        self.child = value


class Not(Unary):
    """
    This is the class for the AST of the not operator.
    """

    pass


class Neg(Unary):
    """
    This is the class for the AST of the neg operator.
    """

    pass


class Binary(Operator):
    """
    This is a base class for all binary expressions
    """

    OPERATOR = ""

    left: Expression
    right: Expression

    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right


class Add(Binary):
    """
    This is the class for the AST of the add operator.
    """

    OPERATOR = "+"

    pass


class Sub(Binary):
    """
    This is the class for the AST of the sub operator.
    """

    OPERATOR = "-"

    pass


class Mul(Binary):
    """
    This is the class for the AST of the mul operator.
    """

    OPERATOR = "*"

    pass


class Div(Binary):
    """
    This is the class for the AST of the div operator.
    """

    OPERATOR = "/"

    pass


class Mod(Binary):
    """
    This is the class for the AST of the mod operator.
    """

    OPERATOR = "%"

    pass


class Equal(Binary):
    """
    This is the class for the AST of the equal operator.
    """

    OPERATOR = "=="

    pass


class NotEqual(Binary):
    """
    This is the class for the AST of the not equal operator.
    """

    OPERATOR = "!="

    pass


class Less(Binary):
    """
    This is the class for the AST of the less operator.
    """

    OPERATOR = "<"

    pass


class LessEqual(Binary):
    """
    This is the class for the AST of the less equal operator.
    """

    OPERATOR = "<="

    pass


class Greater(Binary):
    """
    This is the class for the AST of the greater operator.
    """

    OPERATOR = ">"

    pass


class GreaterEqual(Binary):
    """
    This is the class for the AST of the greater equal operator.
    """

    OPERATOR = ">="

    pass


class And(Binary):
    """
    This is the class for the AST of the and operator.
    """

    OPERATOR = "and"

    pass


class Or(Binary):
    """
    This is the class for the AST of the or operator.
    """

    OPERATOR = "or"

    pass


T = TypeVar("T")


class Const(Expression, Generic[T]):
    """
    This is a base class for the AST of the constant expressions.
    """

    value: T

    def __init__(self, value: T):
        self.value = value


class Numeric(Const[int]):
    """
    This is a class for the AST of the numeric constant expressions.
    """

    pass


class Boolean(Const[bool]):
    """
    This is a class for the AST of the boolean constant expressions.
    """

    pass


class String(Const[str]):
    """
    This is a class for the AST of the string constant expressions.
    """

    pass


class Variable(Expression):
    """
    This is a class for the AST of the variable expressions.
    """

    name: str
    _type: Types

    def __init__(self, name: str, _type: Types):
        self.name = name
        self._type = _type


class Call(Expression):
    """
    This is a class for the AST of the call expressions.
    """

    name: str
    args: List[Expression]

    def __init__(self, name: str, args: List[Expression]):
        self.name = name
        self.args = args


def parse(tokens: List[Token]) -> Expression:
    """
    This is a function for parsing list of tokens to expressions
    """

    root: Optional[Expression] = None

    tokens_iter = iter(tokens)

    for token in tokens_iter:
        if token._type == TokenType.INT:
            if root is None:
                root = Numeric(int(token.value))
            elif isinstance(root, Binary):
                root.right = Numeric(int(token.value))
            elif isinstance(root, Unary):
                root.child = Numeric(int(token.value))
        elif token._type == TokenType.LPAREN:
            parents = []  # list of tokens bounded by parentheses
            counter = 1
            for token in tokens_iter:
                if token._type == TokenType.LPAREN:
                    counter += 1
                elif token._type == TokenType.RPAREN:
                    counter -= 1
                if counter == 0:
                    break
                parents.append(token)
            if isinstance(root, Binary):
                root.left = parse(parents)
            elif isinstance(root, Unary):
                root.child = parse(parents)

    return root


"""
1 + 2 * - ( 1 + 2 )

1

  +
 /
1

  +
 / \
1   2

  +
 / \
1   *
   /
  2

  +
 / \
1   *
   / \
  2   -
      |
      +
     / \
    1   2
"""
