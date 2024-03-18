#!/usr/bin/env python3
"""Import modules for asynchronous function."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function measures the time it takes to run the
    `wait_n` func with `n` coroutines.
    Params:
        n(int): number of coroutines
        max_delay(int): max amount of delay in seconds (random)
    Returns:
        Approximate elapsed time per coroutine(float)
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    return ((time.time() - start_time) / n)
