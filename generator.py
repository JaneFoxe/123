# Напиши генератор even_numbers, который генерирует все чётные числа от 0 до заданного предела.

def even_numbers(a):
    for n in range(0, a + 1):
        if n % 2 == 0:
            yield n


even_numbers_list = even_numbers(10)
for number in even_numbers_list:
    print(number)
