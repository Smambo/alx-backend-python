#!/usr/bin/env python3
"""Import modules for below functions"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotated the function parameters.
    """
    return [(i, len(i)) for i in lst]
