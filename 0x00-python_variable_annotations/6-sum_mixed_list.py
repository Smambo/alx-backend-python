#!/usr/bin/env python3
"""
Below module takes mixed list of ints and floats
and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function takes mixed arguments (int, float) and
    returns their sum as a float.
    """

    total = 0.0

    for i in mxd_lst:
        total += i
    return (total)
