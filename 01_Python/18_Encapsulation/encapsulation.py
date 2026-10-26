
# Program 1: Encapsulation Basics

class Employee:

    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)


employee = Employee("Alex", "AI Engineering", 60000)

# Access public and protected attributes
print("Public name:", employee.name)
print("Protected department:", employee._department)

# Access private-style data through a method
employee.display_details()



#Program 2: Getter and Setter

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    # Getter
    def get_salary(self):
        return self.__salary

    # Setter with validation
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print("Salary updated successfully.")
        else:
            print("Error: Salary must be greater than zero.")


employee = Employee("Alex", 60000)

print("Current salary:", employee.get_salary())

employee.set_salary(75000)
print("Updated salary:", employee.get_salary())

employee.set_salary(-5000)
print("Final salary:", employee.get_salary())



#Program 3: Encapsulation in ML Model Training

class ModelTrainer:
    def __init__(self, model_name, learning_rate, epochs):
        self.model_name = model_name
        self.__learning_rate = learning_rate
        self.__epochs = epochs

    def get_settings(self):
        print("Model:", self.model_name)
        print("Learning rate:", self.__learning_rate)
        print("Epochs:", self.__epochs)

    def set_learning_rate(self, rate):
        if 0 < rate <= 1:
            self.__learning_rate = rate
            print("Learning rate updated.")
        else:
            print("Error: Learning rate must be between 0 and 1.")

    def set_epochs(self, epochs):
        if epochs > 0:
            self.__epochs = epochs
            print("Epochs updated.")
        else:
            print("Error: Epochs must be positive.")

trainer = ModelTrainer("Neural Network", 0.01, 100)

trainer.get_settings()

trainer.set_learning_rate(0.001)
trainer.set_epochs(200)

trainer.get_settings()

trainer.set_learning_rate(2)
trainer.set_epochs(-10)

