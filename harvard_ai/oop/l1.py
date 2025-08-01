# Defining class and creating objects

# Defining class 'Car'
'''
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} is driving.")

# Creating an object
my_car = Car("Toyota", "Red")
my_car.drive()
'''

# Defining class 'Student'
''''
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def show_info(self):
        print(f"{self.name}, Grade {self.grade}")

# Creating an object of student
s1 = Student("Any", "A")
s1.show_info()  
'''

# Encapsulation (Hiding Data)
''''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"Balance: {self.__balance}")

# Creating object
acc = BankAccount(1000)
acc.deposit(500)
acc.show_balance()
'''

# Inheritance
''''
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.speak()  # From Animal
dog.bark()   # From Dog
'''

# Polymorephsim
''''
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

animals = [Cat(), Dog()]
for a in animals:
    a.sound()
'''

# Abstraction
''''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r
    
c = Circle(5)
print(c.area())
'''

# Dunder Method
''''
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("Python 101")
print(b)
'''

''''
# Person class:
    - name
    - age
    print("Name: ", age " ", year old)

# Student:
    - Major
    
# Final display result should be: 
                                Piseth, 22 year old
                                Major: Software Engineering
'''

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"{self.name}, {self.age} years old"
    
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def __str__(self):
        return f"{self.show()}\nMajor: {self.major}"

# Creating an object
s = Student("Piseth", 22, "Software Engineering")
print(s)
# s.show()