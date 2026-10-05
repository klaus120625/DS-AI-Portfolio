##What is a List?

#A list stores multiple values in a single variable.

#Lists are:

#Ordered
#Changeable (mutable)
#Allow duplicate values
#Can contain different data types.

#  Lists  Code 1:
#  Creating, Accessing and Updating a List

students = ["Swarup", "Rahul", "Amit", "Priya"]

print("Students:", students)

# Access elements
print("First student:", students[0])
print("Last student:", students[-1])

# Update an element
students[1] = "Rohan"

print("Updated students:", students)




#  Lists
#  Code 2: List Methods

fruits = ["Apple", "Banana", "Mango"]

print("Original list:", fruits)

# Add an item
fruits.append("Orange")

# Insert an item at a specific position
fruits.insert(1, "Grapes")

# Remove an item
fruits.remove("Banana")

# Sort the list
fruits.sort()

print("Updated list:", fruits)
print("Number of fruits:", len(fruits))


#Store student marks in a list and calculate:

#Total marks
#Average marks
#Highest marks
#Lowest marks
#Number of subjects

#Lists
# Code 3: Practical List Program

marks = [78, 85, 92, 67, 88]

total_marks = sum(marks)
average_marks = total_marks / len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
number_of_subjects = len(marks)

print("Marks:", marks)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Number of Subjects:", number_of_subjects)