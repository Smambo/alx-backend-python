#!/usr/bin/env python3
"""Import modules for below function."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function returns a tuple.
    """
    return (k, v**2)
