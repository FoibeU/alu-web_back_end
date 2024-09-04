#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that returns a function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier function"""

    def multiply(a: float) -> float:
        """multiply function"""
        return a * multiplier

    return multiply