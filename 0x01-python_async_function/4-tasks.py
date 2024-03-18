#!/usr/bin/env python3
"""Import modules for below asynchronous function."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function alters code from `wait_n` into this function.
    Waits for random amounts of time up to `max_delay`
    Returns:
        list of Task objects, sorted in ascending order
    """

    wait_times = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )

    return (sorted(wait_times))
