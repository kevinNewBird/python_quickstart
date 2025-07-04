import concurrent.futures
import os
from concurrent.futures import ThreadPoolExecutor
import time
import random
import threading


def task(n):
    sleep_seconds = random.randint(1, 3)    #随机睡眠时间
    print('线程名称：%s，参数：%s，睡眠时间：%s' % (threading.current_thread().name, n, sleep_seconds))
    time.sleep(sleep_seconds)  # 定义睡眠时间
    return n * n


pool = ThreadPoolExecutor(max_workers=10,thread_name_prefix='ThreadPoolTest2-')

futures = [pool.submit(task, i) for i in range(10)]
for future in concurrent.futures.as_completed(futures):
    result = future.result()
    # print(f"Result: {result}")

print("****************************************")
futures = [pool.submit(task, i) for i in range(20,30)]
for future in concurrent.futures.as_completed(futures):
    result = future.result()

print('cpu:'.format(os.cpu_count()))



