#!/usr/bin/env python3
"""Import modules for asynchronous coroutine."""

from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine asynchronously generates a list comprehension
    that generates a list of floats
    """

    return [num async for num in async_generator()]
