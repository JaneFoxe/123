# def decor_decor(iters):
#     def decor_func(func):
#         import time
#
#         def wrapper(*args, **kwargs):
#             total = 0
#             for i in range(iters):
#                 start = time.time()
#                 res = func(*args, **kwargs)
#                 end = time.time()
#                 total += (end - start)
#             print('[*] Время выполнения: {} секунд.'.format(total/iters))
#             return res
#         return wrapper
#     return decor_func
#
#
# @decor_decor(iters=10)
# def get_result(a, b):
#     result = a * b
#     return result
#
#
# print(get_result(5, 6))
#
import datetime
import functools


def log_function(log_file):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tipmestamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
            res = func(*args, **kwargs)
            with open(log_file, "a") as file:
                file.write(f"Function: {func.__name__}\n"
                           f"Arguments: {args}\n"
                           f"Result: {res}\n"
                           f"Timestamp: {tipmestamp} \n"
                           f"\n")
                return res

        return wrapper

    return decorator


@log_function("log.txt")
def calc_add(a, b):
    return a + b


calc_add(4, 2)
