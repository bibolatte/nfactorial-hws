a = 423
b = 14
sum = a + b
print(sum)

c = "string"
print(c[::-1]) 

str = "bag"
print(len(str))

summary= str + c
print(summary)

char = "a"
if char in "aeuioAOIUE":
    print("vowel")

s = "hello"
if len(s) >= 2:
    new_s = s[-1] + s[1:-1] + s[0]
else:
    new_s = s
print(new_s)

print(s.upper())

len = 12
wid = 13
print(len * wid)

abc = 12
def is_even():
    if abc % 2 == 0:
        print("Even")
is_even()

string = "stringsss"
print(string[:3])

name = "Bibo"
age = "21"
print(f'{name}, {age}')

print(string[2:6])

number = "23"
print(int(number))

print(string*3)

quo = a // b
rem = a % b
print(quo, rem)

floa = a / b
print(floa)

char = "s"
count = 0
for f in string:
    if char == f:
        count += 1
print(count)

text = "He said, \"Hello!\""
print(text)

mult_line = """Hi
There is a code
from backend coure"""
print(mult_line)

base = 2
exponent = 5
result = base ** exponent
print(result)


word = "racecar"
if word == word[::-1]:
    print("yes, it is a polyindrome")
else:
    print("not a palindrome")

str1 = "Listen"
str2 = "Silent"
if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagram")
else:
    print("Not an Anagram")