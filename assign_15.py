#1 task
class Pizza:
    def __init__(self):
        self.ingredients = []
    
    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError

        self.ingredients.append(ingredient)


#2 task
class Elevator:
    def __init__(self):
        self.floor = 1

    def go_up(self, x):
        self.floor += x

    def go_down(self, x):
        if self.floor - x < 0:
            raise ValueError
        self.floor -= x

    def get_current_floor(self):
        return self.floor
    

#3 task
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack == []:
            raise IndexError
        return self.stack.pop()

    def is_empty(self):
        if self.stack == []:
            return True
        return False
        

#4 task
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError
        self.balance -= amount

    def check_balance(self):
        return self.balance


#5 task
class Person:
    def __init__(self, name, age):
        if self.age < 0:
            raise ValueError
        
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


#6 task
class Animal:
    def sound(self):
        return "some noise"

class Dog(Animal):
    def sound(self):
        return "woof"
    
class Cat(Animal):
    def sound(self):
        return "meow"
    

#7 task
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError
        return x / y
    

#8 task
class Car:
    def __init__(self, speed, mileage):
        if speed < 0:
            raise ValueError
        elif mileage < 0:
            raise ValueError
        
        self.speed = speed
        self.mileage = mileage


#9 task
class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def print_students(self):
        for s in self.students:
            print(s.students)


#10 task
class Flight:
    def __init__(self, destination, departure):
        self.dest = destination
        self.depart = departure
        self.passenger = []

    def add_passenger(self, passenger):
        self.passenger.append(passenger)

    def change_destination(self, new_destination):
        self.dest = new_destination

    def delay(self, delay_time):
        self.depart += delay_time


#11 task
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


#12 task
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("wrong dimensions")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Wrong dimensions")
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)


#13 task
class Rectangle:
    def __init__(self, height, width):
        if height <= 0 or width <= 0:
            raise ValueError
    
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        return self.width == self.height


#14 task
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * 3.14

    def circumference(self):
        return 2 * 3.14 * self.radius


#15 task
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if side_a < 0 or side_b < 0 or side_c < 0:
            raise ValueError
        if side_a + side_b <= side_c and side_a + side_c <= side_b and side_b + side_c <= side_a:
            raise ValueError
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        sp = self.perimeter() / 2
        area = (sp * (sp - self.side_a) * (sp - self.side_b) * (sp - self.side_c)) ** 0.5


#16 task
import math
class AbstractShape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(AbstractShape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError
        self.radius = radius
    def area(self):
        return (self.radius ** 2) * 3.14
    def perimeter(self):
        return 2 * self.radius * 3.14

class Rectangle(AbstractShape):
    def __init__(self, height, width):
        if height <= 0 or width <= 0:
            raise ValueError
    def area(self):
        return self.height * self.width

class Triangle(AbstractShape):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
    
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))


#17 task



#18 task
class Product:
    def __init__(self, name, price, quantity):
        if price < 0:
            raise ValueError
        if quantity < 0:
            raise ValueError
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        if quantity <= 0:
            raise ValueError
        self.quantity += quantity
    
    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError
        if quantity > self.quantity:
            raise ValueError
        
        self.quantity -= quantity
        total_cost = quantity * self.price
        return total_cost
    
    def check_stock(self):
        return self.quantity


#19 task
class VideoGame:
    def __init__(self, title, genre, rating):
        if rating < 0 or rating > 10:
            raise ValueError
        
        self.title = title
        self.genre = genre
        self.rating = rating
    def change_rating(self, rating):
        if rating < 0 or rating > 10:
            raise ValueError
        
        old_rating = self.rating
        self.rating = rating
        print(f"game genre '{self.title}' modified with {old_rating} to {self.rating}")
    def change_genre(self, genre):
        old_genre = self.genre
        self.genre = genre
        print(f"Game genre '{self.title}' modified with '{old_genre}' to '{self.genre}'")
    def display_details(self):
        print(f"Name: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Raiting: {self.rating}/10")
        print("-" * 30)


#20 task
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    pass

class Student(Person):
    pass

class School:
    def __init__(self):
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def print_all(self):
        for teacher in self.teachers:
            print(f"Teacher: {teacher.name}, {teacher.age}")
        for student in self.students:
            print(f"Student: {student.name}, {student.age}")


#21 task
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            raise ValueError
        return self.cards.pop()

    def count(self):
        return len(self.cards)