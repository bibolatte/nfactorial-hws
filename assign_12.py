from typing import List, Any, Dict, Set, Generator


#1 task
def squares(n: int):
    return [x ** 2 for x in range(n)]


#2 task
def unique_squares(numbers: List[int]) -> Set[int]:
    return {x ** 2 for x in numbers}
print(unique_squares([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))


#3 task
def char_counts(text: str) -> Dict[str, int]:
    return {char: text.count(char) for char in text}
char_counts("hello")


#4 task
def flatten(nested_list: List[List[Any]]) -> List[Any]:
    return [item for sublist in nested_list for item in sublist]


#5 task
def squares_gen(n: int) -> Generator[int, None, None]:
    return (x**2 for x in range(n))


#6 task
def odd_squares(n: int) -> Set[int]:
    return {x**2 for x in range(n) if x % 2 != 0}


#7 task
def index_map(text: str) -> dict[str, int]:
    return {char: i for i, char in enumerate(text)}


#8 task
def unique_values(nested_list: List[List[Any]]) -> Set[Any]:
    return {item for sublist in nested_list for item in sublist}


#9 tsak
def fibonacci_gen(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b 


#10 task
def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    return {v: k for k, v in d.items()}


#11 task
def primes(n: int) -> List[int]:
    return [x for x in range(2, n + 1) 
            if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]


#12 task
def intersection(sets: List[Set[Any]]) -> Set[Any]:
    if not sets:
        return set()
    return {item for item in sets[0] if all(item in s for s in sets[1:])}


#13 task
def get_factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def factorials_gen(n: int) -> Generator[int, None, None]:
    return (get_factorial(x) for x in range(1, n + 1))


#14 task
def str_lengths(strings: List[str]) -> Dict[str, int]:
    # Ключ — сама строка, значение — результат функции len()
    return {s: len(s) for s in strings}


#15 task
def transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    if not matrix: return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


#16 task
def reverse_gen(lst: List[Any]) -> Generator[Any, None, None]:
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]


#17 task
def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    return {len(w): [word for word in words if len(word) == len(w)] for w in words}


#18 task
def common_elements(lists: List[List[Any]]) -> Set[Any]:
    if not lists: return set()
    return {x for x in lists[0] if all(x in l for l in lists[1:])}


#19 task
def primes_gen(n: int) -> Generator[int, None, None]:
    return (x for x in range(2, n + 1) 
            if all(x % i != 0 for i in range(2, int(x**0.5) + 1)))


#20 task
def list_to_dict(lst: List[Any]) -> Dict[int, Any]:
    return {i: val for i, val in enumerate(lst)}

