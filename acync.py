import asyncio


async def worker(task_id, delay):
    print(f'Task {task_id} started')
    await asyncio.sleep(delay)
    print(f'Task {task_id} completed')


async def main():
    tasks = [
        worker(1, 2),
        worker(2, 1),
        worker(3, 3)
    ]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())