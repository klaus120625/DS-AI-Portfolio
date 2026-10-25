#   Program 1: Single Inheritance

class Animal:
    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    def bark(self):
        print("Dog is barking.")


my_dog = Dog()

my_dog.eat()
my_dog.bark()



# Program 2: Multilevel Inheritance

class Person:
    def introduce(self):
        print("I am a person.")


class Student(Person):
    def study(self):
        print("I am studying Python.")


class AIStudent(Student):
    def learn_ai(self):
        print("I am learning Artificial Intelligence.")


# Create an object of the child class
student = AIStudent()

# Access methods from all three levels
student.introduce()
student.study()
student.learn_ai()


# Day 15 - Program 3: Hierarchical Inheritance

class Vehicle:
    def start(self):
        print("Vehicle is starting.")


class Car(Vehicle):
    def drive(self):
        print("Car is driving.")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding.")


# Create objects
my_car = Car()
my_bike = Bike()

# Car uses its own method and the inherited method
my_car.start()
my_car.drive()

# Bike uses its own method and the inherited method
my_bike.start()
my_bike.ride()

