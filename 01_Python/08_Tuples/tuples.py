#What is a Tuple?

#A tuple is a collection of values, similar to a list, but a tuple is immutable—once created, its elements cannot be changed.

# Tuples
# Code 1: Creating and Accessing a Tuple

student = ("Swarup", 22, "Data Science")

print("Student details:", student)

print("Name:", student[0])
print("Age:", student[1])
print("Course:", student[2])

print("Number of details:", len(student))
print("Data type:", type(student))


#Tuple Methods & Operations

#Tuples have fewer methods than lists because they are immutable.

# Day 8 - Tuples
# Code 2: Tuple Methods and Operations

numbers = (10, 20, 30, 20, 40, 20)

print("Tuple:", numbers)

# Count how many times 20 appears
print("Count of 20:", numbers.count(20))

# Find the position of 30
print("Position of 30:", numbers.index(30))

# Check whether a value exists
print("Is 40 present?", 40 in numbers)

# Find the total
print("Total:", sum(numbers))


#Store fixed information about a product and unpack the tuple into separate variables.
#  Tuples
# Code 3: Practical Tuple Program

product = ("Laptop", 65000, "Electronics", 2)

name, price, category, warranty = product

print("Product Name:", name)
print("Price:", price)
print("Category:", category)
print("Warranty:", warranty, "years")

# Calculate price after a 10% discount
discounted_price = price - (price * 0.10)

print("Price after 10% discount:", discounted_price)