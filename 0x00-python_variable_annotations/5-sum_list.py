#!/usr/bin/env python3
"""
Below module returns the sum of a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function takes a list of floats as arguments
    and returns their sum.
    """
    total = 0.0

    for i in input_list:
        total += i
    return (total)
