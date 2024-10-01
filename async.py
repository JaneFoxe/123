from _thread import start_new_thread

# threadId = 1
#
# def factorial(n):
#   global threadId
#   if n < 1:
#       print("Thread", threadId )
#       threadId += 1
#       return 1
#   else:
#       returnNumber = n * factorial( n - 1 )  # рекусрсивынй вызов
#       print(str(n) + '! = ' + str(returnNumber))
#       return returnNumber
#
# start_new_thread(factorial,(5, ))
# start_new_thread(factorial,(4, ))
#
# c = input("Waiting for threads to return...\n")

# Напиши скрипт, который создает 3 потока и каждый поток прибавляет к глобальному счётчику 100 раз
# (то есть так: for _ in range(100): counter += 1). Используй mutex для синхронизации доступа к общим ресурсам.
# В конце просто принтани результат глобального счётчика (counter).

import threading

counter = 0
mutex = threading.Lock()

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting " + self.name)
        add_one()
        print("Exiting " + self.name)


def add_one():
    global counter
    for i in range(100):
        mutex.acquire()
        counter += 1
        mutex.release()


# Создать треды
thread1 = myThread("Thread 1")
thread2 = myThread("Thread 2")
thread3 = myThread("Thread 3")

# Запустить треды
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
print(counter)
