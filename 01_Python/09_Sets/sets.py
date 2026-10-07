 # Sets
 # Creating and Accessing a Set

numbers = {10, 20, 30, 20, 40, 10}

print("Set:", numbers)

print("Number of unique values:", len(numbers))

print("Is 30 present?", 30 in numbers)
print("Is 50 present?", 50 in numbers)


# Sets
# Set Operations

python_students = {"Swarup", "Rahul", "Amit", "Priya"}
sql_students = {"Swarup", "Priya", "Neha", "Rohan"}

print("Python Students:", python_students)
print("SQL Students:", sql_students)

# Students in both courses
print("Students in both:", python_students.intersection(sql_students))

# Students in either course
print("Students in either:", python_students.union(sql_students))

# Students only in Python
print("Only Python:", python_students.difference(sql_students))

# Students only in SQL
print("Only SQL:", sql_students.difference(python_students))


# Sets
# Practical Customer Analysis

january_customers = {101, 102, 103, 104, 105}
february_customers = {103, 104, 105, 106, 107}

# All unique customers
all_customers = january_customers.union(february_customers)

# Customers who returned
returning_customers = january_customers.intersection(february_customers)

# New customers in February
new_customers = february_customers.difference(january_customers)

# Customers who did not return
lost_customers = january_customers.difference(february_customers)

print("January Customers:", january_customers)
print("February Customers:", february_customers)

print("All Unique Customers:", all_customers)
print("Returning Customers:", returning_customers)
print("New Customers:", new_customers)
print("Lost Customers:", lost_customers)