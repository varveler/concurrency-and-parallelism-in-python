#!/usr/bin/env python3
# countasync.py

import asyncio

async def count():
    await asyncio.sleep(1)
    print("one")
    return 1

async def count_two():
    await asyncio.sleep(5)
    print("Two")
    return 2


async def main():
    await asyncio.gather(count(), count_two(), count(), count_two())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
