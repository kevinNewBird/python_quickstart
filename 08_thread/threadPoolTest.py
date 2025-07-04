import concurrent.futures
import time


def task(n):
    time.sleep(2)  # 模拟耗时操作
    return n * n


# 创建一个具有5个工作线程的线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # 提交多个任务到线程池
    futures = [executor.submit(task, i) for i in range(10)]

    # 获取所有任务的结果（可选）
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(f"Result: {result}")
