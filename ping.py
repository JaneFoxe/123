import asyncio
import aiohttp
import time

URLS = [
    "https://adventuretime.mult-fan.tv/page.php?id=411a&voice=4&autoplay=1",
    "https://easyoffer.ru/question/781",
    "https://habr.com/ru/articles/417215/",
    "https://chatgpt.com/",
    "https://loh"
]


async def get_ping(url):
    start_time = time.time()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    time_spent = time.time() - start_time
                    print(f"Пинг {url} завершен за {time_spent} секунд.")
                else:
                    print(f"Ошибка {response.status} при доступе к {url}")
    except Exception as e:
        print(f"Не удалось пинговать {url}. Ошибка: {str(e)}")


async def main():
    tasks = [get_ping(url) for url in URLS]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
