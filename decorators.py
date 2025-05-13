# from time import time
# def run_time(func):
#     def wrapper(*args):
#         a = time()
#         result = func(*args)
#         b = time()
#         print(b-a)
#         return result
#     return wrapper
#
# @run_time
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(2))
from time import time

def run_time(func):
    def wrapper(*args):
        a = time()
        result = func(*args)  # Properly unpack *args
        b = time()
        print(f"Execution time: {b - a} seconds")
        return result  # Return the result of the function
    return wrapper

@run_time
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))
