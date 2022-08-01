import asyncio


async def p(n):
    while True:
        print(n)
        # 在python的协程中想要sleep的话必须使用asyncio的sleep
        await asyncio.sleep(1)


async def main():
    for i in range(100000):
        # await p(i) 阻塞 1.将协程运行起来 2.阻塞协程直到返回结果
        # print("hello")
        # python的单个协程占用内存少 go的协程写起来简单
        asyncio.create_task(p(i))
        # 内存变化不大
    await asyncio.sleep(10000)
    # import time


asyncio.run(main())
