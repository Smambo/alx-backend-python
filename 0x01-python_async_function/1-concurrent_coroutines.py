#!/usr/bin/env python3
"""Import modules for below asynchronous function."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine takes in two int arguments. Spawns `wait_random` `n` times
    with the specified `max_delay`
    Params:
        n(int)
        max_delay(int)
    Returns:
        list of all delays (float values) in ascending order
        without using sort() because of concurrency
    """

    wait_times = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )

    return (sorted(wait_times))
