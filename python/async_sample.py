import asyncio


async def hello_world():
    print("Hello World!")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())

loop = asyncio.get_event_loop()
loop_2 = asyncio.get_event_loop()
print("loop is loop2 ")  # True
print(loop is loop_2)  # True
