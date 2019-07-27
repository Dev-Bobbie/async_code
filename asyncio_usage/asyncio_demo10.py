#!/usr/bin/env python
"""
 Created by bobbie at 2018/11/25.
"""
import asyncio


async def async_hello(future):
    print('async hello')
    await asyncio.sleep(1)
    future.set_result('Hello World')


def hello():
    ft = asyncio.Future()
    asyncio.ensure_future(async_hello(ft))
    # 重点就是这里，返回一个Future
    return ft


async def run():
    print('Run ...')
    r = await hello()
    print(r)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()