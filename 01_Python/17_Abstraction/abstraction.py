
#Program 1: Abstract Classes

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# Create a Rectangle object
rectangle = Rectangle(10, 5)

print("Rectangle area:", rectangle.calculate_area())



# Day 17 - Program 2: Abstraction with Multiple Shapes

from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


# Create objects
rectangle = Rectangle(10, 5)
circle = Circle(7)

print("Rectangle area:", rectangle.calculate_area())
print("Circle area:", round(circle.calculate_area(), 2))

# Program 3: AI Model Interface using Abstraction

from abc import ABC, abstractmethod


class AIModel(ABC):

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass


class LinearRegressionModel(AIModel):

    def train(self):
        print("Training Linear Regression Model...")

    def predict(self):
        print("Predicting House Prices.")


class ImageClassifier(AIModel):

    def train(self):
        print("Training Image Classification Model...")

    def predict(self):
        print("Predicting Image Category.")


# Create objects
models = [
    LinearRegressionModel(),
    ImageClassifier()
]

# Call common methods
for model in models:
    model.train()
    model.predict()
    print("-" * 30)