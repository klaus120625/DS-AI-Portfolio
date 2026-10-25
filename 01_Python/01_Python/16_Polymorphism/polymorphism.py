
# Program 1: Polymorphism

class Dog:
    def sound(self):
        print("Dog barks.")


class Cat:
    def sound(self):
        print("Cat meows.")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


#Program 2: Method Overriding

class Animal:
    def sound(self):
        print("Animals make sounds.")


class Dog(Animal):
    def sound(self):
        print("Dog barks.")


class Cat(Animal):
    def sound(self):
        print("Cat meows.")


dog = Dog()
cat = Cat()
animal = Animal()

animal.sound()
dog.sound()
cat.sound()


#Program 3: Polymorphism with a Loop

class LinearRegressionModel:
    def predict(self):
        print("Predicting a continuous value.")


class ClassificationModel:
    def predict(self):
        print("Predicting a class label.")


class ImageClassificationModel:
    def predict(self):
        print("Predicting an image category.")


# Store different model objects in a list
models = [
    LinearRegressionModel(),
    ClassificationModel(),
    ImageClassificationModel()
]

# Call the same method on every object
for model in models:
    model.predict()

