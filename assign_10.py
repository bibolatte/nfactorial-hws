#1 task
def operation(func, x: int, y: int) -> int:
    return func(x, y)

def sum(a, b):
    count = 0
    for x in range(a, b):
        count += x
    return count


#2 task
def my_map(func, my_list: list) -> list:
    result = map(func, my_list)
    return result
    
data = [1, 2, 4, 6, 9]
doubled = my_map(lambda x: x + x, data)


#3 task тут не смог использовать фильтр
def filter_even_numbers(my_list):
    new_list = []
    for n in my_list:
        if n % 2 == 0:
            new_list.append(n)
    return new_list


#4 task
from functools import reduce

def recursive_factorial(n: int) -> int:
    return reduce(lambda x, y: x * y, range(1, n + 1))


#5 task
import time

def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__, (end_time - start_time))
        return result
    return wrapper

@timeit_decorator
def long_task():
    time.sleep(2)
    return "Ready - Ready?"


#6 task
def compose(*funcs):
    def wrapper(x):
        result = x
        for f in funcs:
            result = f(result)
        return result
    return wrapper

def double(n):
    return n * 2

def incertion(n):
    return n + 1

def square(n):
    return n ** 2

all = compose(double, incertion, square)
result = all(5)
print(result)


#7 task
def partial(func, *args):
    def wrapper(*new_args):
        all = args + new_args 
        return func(*all)
    return wrapper

def sum_three(a, b, c):
    return a + b + c
add_to_ten = partial(sum_three, 10) 

print(add_to_ten(5, 2)) 


#8 task
from functools import reduce

def factorial_reduce(n: int) -> int:
    if n < 2:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))


#9 task
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print({args})
            return cache[args]
        result = func(*args)
        
        cache[args] = result
        
        return result
    return wrapper

def expensive_calculation(n):
    return n ** n

smart_func = memoize(expensive_calculation)


#10 task
def my_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    
    if initializer is not None:
        res = initializer
    else:
        res = next(it)

    for x in it:
        res = func(res, x)
        
    return res


#11 task
def sort_by_last_letter(words: list) -> list:
    return sorted(words, key=lambda word: word[-1])

list_of_words = ['apple', 'banana', 'cherry', 'date']
result = sort_by_last_letter(list_of_words)


#12 task
def recursive_reverse(my_list: list) -> list:
    if len(my_list) <= 1:
        return my_list

    return recursive_reverse(my_list[1:]) + [my_list[0]]


#13 task
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' was called {wrapper.calls} times.")
        return result
    
    wrapper.calls = 0
    return wrapper


#14 task
from functools import reduce

def find_max(numbers: list) -> int:
    if not numbers:
        return None
    
    return reduce(lambda x, y: x if x > y else y, numbers)


#15 task
def remove_elements(my_list: list, element) -> list:
    result = filter(lambda x: x != element, my_list)
    
    return list(result)


#16 task
def repeat(n: int):
    def wrapper(s: str) -> str:
        return s * n
    
    return wrapper


#17 task
def recursive_sum(my_list: list) -> int:
    if not my_list:
        return 0
    
    return my_list[0] + recursive_sum(my_list[1:])


#18 task
def add_two_lists(list1: list, list2: list) -> list:
    result = map(lambda x, y: x + y, list1, list2)
    
    return list(result)