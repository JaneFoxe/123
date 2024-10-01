import time


def coroutine():
    print("Запустили корутину")
    while True:
        data = yield
        if data is None:
            break
        print(f"Данные: {data}")


def main():
    cor = coroutine()
    next(cor)

    for i in range(5):
        cor.send(i)
        time.sleep(2)

    cor.send(None)


if __name__ == "__main__":
    main()
