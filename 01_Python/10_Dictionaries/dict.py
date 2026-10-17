# Day 10 - Dictionaries
# Creating, Accessing and Updating a Dictionary

student = {
    "name": "Swarup",
    "age": 22,
    "course": "Data Science",
    "city": "Kolhapur"
}

print("Student Details:", student)

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

student["age"] = 23
student["city"] = "Pune"

print("Updated Student Details:", student)





# Day 10 - Dictionaries
# Dictionary Methods

employee = {
    "name": "Rahul",
    "department": "IT",
    "salary": 45000,
    "city": "Pune"
}

# Display all keys
print("Keys:", employee.keys())

# Display all values
print("Values:", employee.values())

# Display key-value pairs
print("Items:", employee.items())

# Safely access a value
print("Salary:", employee.get("salary"))

# Add or update a value
employee.update({"salary": 50000, "experience": 2})

# Remove a key
employee.pop("city")

print("Updated Employee:", employee)



# Day 10 - Dictionaries
# Practical Employee Salary Analysis

employees = {
    "Rahul": 45000,
    "Priya": 55000,
    "Amit": 40000,
    "Swarup": 60000
}

# Display employee salaries
print("Employee Salary Details:")

for name, salary in employees.items():
    print(name, ":", salary)

# Calculate salary statistics
total_salary = sum(employees.values())
average_salary = total_salary / len(employees)
highest_paid = max(employees, key=employees.get)
lowest_paid = min(employees, key=employees.get)

print("\nTotal Salary:", total_salary)
print("Average Salary:", average_salary)
print("Highest Paid Employee:", highest_paid)
print("Highest Salary:", employees[highest_paid])
print("Lowest Paid Employee:", lowest_paid)
print("Lowest Salary:", employees[lowest_paid])

