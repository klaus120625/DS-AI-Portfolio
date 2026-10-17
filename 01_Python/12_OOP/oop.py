# Day 12 - OOP
#Creating a Class and Object

class Student:
    def display(self):
        print("Student Name: Swarup")
        print("Course: Data Science")
        print("Status: Learning Python")


# Create an object
student1 = Student()

# Call the method
student1.display()

# Day 12 - OOP
# Constructor and self

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("-" * 25)


student1 = Student("Swarup", 22, "Data Science")
student2 = Student("Rahul", 23, "Machine Learning")

student1.display()
student2.display()

# Day 12 - OOP
# Student Marks Analyzer

class MarksAnalyzer:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def display_report(self):
        average = self.calculate_average()

        print("Student:", self.name)
        print("Marks:", self.marks)
        print("Average:", round(average, 2))
        print("Highest Marks:", max(self.marks))
        print("Lowest Marks:", min(self.marks))

        if average >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


student1 = MarksAnalyzer("Swarup", [78, 85, 92, 67, 88])
student1.display_report()