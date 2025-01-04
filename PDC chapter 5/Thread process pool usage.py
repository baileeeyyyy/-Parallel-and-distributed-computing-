#Event loop statement

import asyncio
import time
import random

def task_a(end_time, loop):
    print("Task A called")
    time.sleep(random.randint(0, 5))
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, task_b, end_time, loop)
    else:
        loop.stop()


def task_b(end_time, loop):
    print("Task B called")
    time.sleep(random.randint(3, 7))
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, task_c, end_time, loop)
    else:
        loop.stop()


def task_c(end_time, loop):
    print("Task C called")
    time.sleep(random.randint(5, 10))
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, task_a, end_time, loop)
    else:
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    end_loop = loop.time() + 60  
    loop.call_soon(task_a, end_loop, loop)  
    loop.run_forever()
    loop.close()
