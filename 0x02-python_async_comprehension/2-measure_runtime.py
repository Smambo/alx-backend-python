#!/usr/bin/env python3
"""Import module for below asynchronous function."""

import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine executes `aync_comprehension` 4 times and returns
    total runtime.
    """

    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return (time.time() - start_time)
