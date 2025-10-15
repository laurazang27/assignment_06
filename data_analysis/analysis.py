#!/usr/bin/env python
"""data_analysis.analysis

Small utilities for data-analysis demos.

This module exposes:
- factorial(n): compute factorial of a non-negative integer with input validation.

Example
-------
Run from the command line::

  python3 analysis.py

"""
from __future__ import annotations
from typing import Any


def factorial(n: int) -> int:
  """Return n! for n a non-negative integer.

  Raises:
    TypeError: if n is not an int.
    ValueError: if n is negative.
  """
  if not isinstance(n, int):
    raise TypeError("factorial() only accepts integers")
  if n < 0:
    raise ValueError("factorial() not defined for negative values")
  if n in (0, 1):
    return 1
  return n * factorial(n - 1)


def main() -> None:
  """Simple CLI entry point that prints factorial(5)."""
  print(factorial(5))  # 120


if __name__ == "__main__":
  main()

