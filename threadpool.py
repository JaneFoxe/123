# Task: Создай скрипт, создает пул потоков с ThreadPoolExecutor с 4 рабочими потоками. Затем отправляй 4 задачи на
# выполнение в пул потоков с помощью executor.submit(). Как только все задачи отправлены в пул, ждём их завершения с
# помощью concurrent.futures.wait(). Задачи не обязательно писать, просто создай воркер с таск айди и принтуй внутри,
# что выполнилось. Типо так: def worker(task_id): print(f"task with id {task_id}" done)

import concurrent.futures
import time


def worker(task_id):
    # time.sleep(2)
    print(f"task with id {task_id} done")


executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
futures = [executor.submit(worker, i) for i in range(1, 5)]

concurrent.futures.wait(futures)
