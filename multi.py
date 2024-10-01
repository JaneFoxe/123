import multiprocessing
import time


def worker(task_id):
    print(f'start {task_id}')
    time.sleep(2)
    print(f'end {task_id}')


if __name__ == '__main__':
    process_jobs = []
    for i in range(1, 5):
        p = multiprocessing.Process(target=worker, args=(i,))
        process_jobs.append(p)
        p.start()
    for p in process_jobs:
        p.join()


if __name__ == '__main__':
    task_id = [1, 2, 3, 4]
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(worker, task_id)
