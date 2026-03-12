#1 exercise
def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1

    return True


#2 exercise
def nth_fibonacci(n: int) -> int:
    current_val = 0
    next_val = 1
    if n == 0:
        return 0
    
    i = 1

    while i < n:
        sum_val = current_val + next_val
        
        current_val = next_val
        next_val = sum_val
        
        i += 1
    return current_val


#3 exercise
def factorial(n: int) -> int:
    if n == 0:
        return 1
    
    current_val = 1

    i = 1
    while i <= n:
        current_val *= i
        i += 1
    return current_val


#4
def count_vowels(s: str) -> int:
    v = "aieuoAIEUO"
    count = 0
    
    for char in s:
        if char in v:
            count += 1
    return count


#5 exericse
def sum_of_digits(n: int) -> int:
    string_n = str(n)
    sum_num = 0

    for char in string_n:
        digit = int(char)
        sum_num = sum_num + digit
    return sum_num


#6 exercise
def reverse_string(s: str) -> str:
    print(s[::-1])


#7 exercise
def sum_of_squares(n: int) -> int:
    if n == 0:
        return 0
    i = 1
    square = 0
    while i <= n:
        square = square + i**2
        i += 1
    return square


#8 exercise
def collatz_sequence_length(n: int) -> int:
    if n == 0:
        return 0
    if n % 2 == 0:
        n = n / 2
        return n
    else:
        n = 3*n + 1
        return n


#9 exercise
def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


#10 exer
def count_words(s: str) -> int:
    count = 0
    for i in s:
        split = " "
        if i == split:
            count += 1
    return count + 1


#11 exercise
def is_palindrome(s: str) -> bool:
    return s == s[::-1]


#12 exercise
def sum_of_multiples(n: int, x: int, y: int) -> int:
    total_sum = 0
    current_num = 1
    while current_num <= n:
        if current_num % x == 0 or current_num % y == 0:
            total_sum += current_num
        current_num += 1
    return total_sum


#13 exercise
def gcd(a: int, b: int) -> int:
    i = 1
    gcd = 0
    while i <= a:
        if a % i == 0 and b % i == 0:
            gcd = i
        i += 1
    return gcd


#14 exercise
def lcm(a: int, b: int) -> int:
    i = 1
    gcd = 0
    while i <= a:
        if a % i == 0 and b % i == 0:
            gcd = i
        i += 1
    lcm = (a * b) // gcd
    return lcm


#15 exercise
def count_characters(s: str, c: str) -> int:
    count = 0
    i = 0
    for i in s:
        if i == c:
            count += 1
    return count


#16
def digit_count(n: int) -> int:
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


#17 exercise
def is_power_of_two(n: int) -> bool:
    if n == 1:
        return True
    
    i = 2
    while i <= n:
        if i == n:
            return True
        i *= 2

    return False


#18 exercise
def sum_of_cubes(n: int) -> int:
    i = 1
    total = 0
    while i <= n:
        total = total + i ** 3
        i += 1
    return total


#19 exercise
def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    
    i = 1
    while i * i <= n:
        if i*i == n:
            return True
        i += 1
print(is_perfect_square(9))


#20 exercise
def is_armstrong_number(n: int) -> bool:
    s = str(n)
    total = 0
    power = len(s)
    for char in s:
        digit = int(char)
        total += digit ** power
    return total == n