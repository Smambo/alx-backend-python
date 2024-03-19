#!/usr/bin/env python3
"""Import modules for the below async generator."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously yields a random float
    between 0 & 10, with a one second delay.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
