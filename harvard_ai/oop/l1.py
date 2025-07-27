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

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

animals = [Cat(), Dog()]
for a in animals:
    a.sound()