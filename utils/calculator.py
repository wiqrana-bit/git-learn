
# added format comment to the end of the file to test formatting tools
"""Basic calculator utilities.

Provides simple arithmetic functions, a small `Calculator` class,
and a safe `evaluate()` for arithmetic expressions using `ast`.
"""
from __future__ import annotations

import ast
import operator
from typing import Union

Number = Union[int, float]

_OPERATORS = {
	ast.Add: operator.add,
	#ast.Sub: operator.sub,
	#ast.Mult: operator.mul,
	#ast.Div: operator.truediv,
	#ast.Pow: operator.pow,
	#ast.Mod: operator.mod,
}


def _eval_node(node: ast.AST) -> Number:
	if isinstance(node, ast.BinOp):
		left = _eval_node(node.left)
		right = _eval_node(node.right)
		op_type = type(node.op)
		func = _OPERATORS.get(op_type)
		if func is None:
			raise ValueError(f"Unsupported operator: {op_type.__name__}")
		return func(left, right)

	if isinstance(node, ast.UnaryOp):
		operand = _eval_node(node.operand)
		if isinstance(node.op, ast.USub):
			return -operand
		if isinstance(node.op, ast.UAdd):
			return +operand
		raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")

	if isinstance(node, ast.Constant):
		if isinstance(node.value, (int, float)):
			return node.value
		raise ValueError("Only int/float constants are supported")

	raise ValueError(f"Unsupported expression node: {type(node).__name__}")


def evaluate(expression: str) -> Number:
	"""Safely evaluate a simple arithmetic expression and return a number.

	Supported operators: +, -, *, /, %, ** and unary +/-. Parentheses are allowed.
	"""
	tree = ast.parse(expression, mode="eval")
	return _eval_node(tree.body)


def add(a: Number, b: Number) -> Number:
	return a + b


def subtract(a: Number, b: Number) -> Number:
	return a - b


def multiply(a: Number, b: Number) -> Number:
	return a * b


def divide(a: Number, b: Number) -> Number:
	if b == 0:
		raise ZeroDivisionError("division by zero")
	return a / b


def power(a: Number, b: Number) -> Number:
	return a ** b


class Calculator:
	"""Simple calculator wrapper exposing functional API as methods."""

	@staticmethod
	def add(a: Number, b: Number) -> Number:
		return add(a, b)

	@staticmethod
	def subtract(a: Number, b: Number) -> Number:
		return subtract(a, b)

	@staticmethod
	def multiply(a: Number, b: Number) -> Number:
		return multiply(a, b)

	@staticmethod
	def divide(a: Number, b: Number) -> Number:
		return divide(a, b)

	@staticmethod
	def power(a: Number, b: Number) -> Number:
		return power(a, b)

	@staticmethod
	def evaluate(expression: str) -> Number:
		return evaluate(expression)


__all__ = [
	"add",
	"subtract",
	"multiply",
	"divide",
	"power",
	"evaluate",
	"Calculator",
]


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description="Evaluate a simple arithmetic expression or perform an operation.")
	parser.add_argument("expr", help="Expression to evaluate (e.g. '2 + 2')")
	args = parser.parse_args()
	try:
		result = evaluate(args.expr)
	except Exception as exc:  # keep errors visible for CLI use
		raise
	else:
		print(result)

# added format comment to the end of the file to test formatting tools