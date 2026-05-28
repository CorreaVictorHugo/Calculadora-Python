"""Safe arithmetic evaluator used by the calculator interface."""

from __future__ import annotations

import ast
import operator
from dataclasses import dataclass


class CalculatorError(ValueError):
    """Raised when the expression cannot be calculated."""


@dataclass(frozen=True)
class _Operator:
    symbol: str
    function: object


_BINARY_OPERATORS = {
    ast.Add: _Operator("+", operator.add),
    ast.Sub: _Operator("-", operator.sub),
    ast.Mult: _Operator("*", operator.mul),
    ast.Div: _Operator("/", operator.truediv),
    ast.Mod: _Operator("%", operator.mod),
}

_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def calculate(expression: str) -> int | float:
    """Calculate a basic arithmetic expression without using eval."""
    expression = expression.strip()

    if not expression:
        raise CalculatorError("Digite uma expressao.")

    try:
        tree = ast.parse(expression, mode="eval")
        result = _evaluate_node(tree.body)
    except CalculatorError:
        raise
    except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as exc:
        raise CalculatorError("Expressao invalida.") from exc

    return _normalize_result(result)


def _evaluate_node(node: ast.AST) -> int | float:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPERATORS:
        operand = _evaluate_node(node.operand)
        return _UNARY_OPERATORS[type(node.op)](operand)

    if isinstance(node, ast.BinOp) and type(node.op) in _BINARY_OPERATORS:
        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)

        if isinstance(node.op, (ast.Div, ast.Mod)) and right == 0:
            raise CalculatorError("Nao e possivel dividir por zero.")

        operator_info = _BINARY_OPERATORS[type(node.op)]
        return operator_info.function(left, right)

    raise CalculatorError("Use apenas numeros e operadores basicos.")


def _normalize_result(value: int | float) -> int | float:
    if isinstance(value, float) and value.is_integer():
        return int(value)

    return round(value, 10) if isinstance(value, float) else value
