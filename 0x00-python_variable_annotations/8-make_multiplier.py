#!/usr/bin/env python3
"""Import module for below function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function takes a float multiplier and returns
    a function that multiplies a float by a multiplier.
    """
    return lambda k: k * multiplier
