#!/usr/bin/env python3
"""Write a type-annotated function sum_list.
"""
from typing import List


def sum_lists(input_list: List[float]) -> float:
    """Takes a list of floats and returns their sum."""
    return sum(input_list)