#!/usr/bin/env python3
"""Import modules for below function"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augmented code with correct duck-typed annotations."""
    if lst:
        return lst[0]
    else:
        return None
