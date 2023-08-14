import asyncio


async def func_a():
    print("first in func_a!")
    await asyncio.sleep(2)
    print("second in func_a!")
    await asyncio.sleep(2)
    print("third in func_a!")


async def func_b():
    print("first in func_b!")
    await asyncio.sleep(2)
    print("second in func_b!")
    await asyncio.sleep(2)
    print("third in func_b!")


tasks = [asyncio.ensure_future(func_a()), asyncio.ensure_future(func_b())]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
