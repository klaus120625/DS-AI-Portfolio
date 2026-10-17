
# Day 11 - Functions
# Define and Call Functions

def greet():
    print("Hello, Swarup!")
    print("Welcome to Python Functions.")

def show_course():
    print("Course: Data Science")
    print("Language: Python")

# Call the functions
greet()
print()
show_course()



# Day 11 - Functions
# Parameters and Return Values

def calculate_total(price, quantity):
    total = price * quantity
    return total

def calculate_discount(total, discount_percent):
    discount = total * discount_percent / 100
    final_price = total - discount
    return final_price

# Calculate product cost
price = 1500
quantity = 3

total = calculate_total(price, quantity)
final_price = calculate_discount(total, 10)

print("Price per Item:", price)
print("Quantity:", quantity)
print("Total Amount:", total)
print("Discount:", "10%")
print("Final Amount:", final_price)



# Day 11 - Functions
# Practical Salary Calculator

def calculate_bonus(salary, bonus_percent):
    bonus = salary * bonus_percent / 100
    return bonus

def calculate_annual_salary(monthly_salary):
    annual_salary = monthly_salary * 12
    return annual_salary

def calculate_total_annual_income(monthly_salary, bonus_percent):
    annual_salary = calculate_annual_salary(monthly_salary)
    bonus = calculate_bonus(annual_salary, bonus_percent)
    return annual_salary + bonus

# Employee details
employee_name = "Swarup"
monthly_salary = 50000
bonus_percent = 10

# Calculations
annual_salary = calculate_annual_salary(monthly_salary)
bonus = calculate_bonus(annual_salary, bonus_percent)
total_income = calculate_total_annual_income(
    monthly_salary, bonus_percent
)

# Display results
print("Employee Name:", employee_name)
print("Monthly Salary:", monthly_salary)
print("Annual Salary:", annual_salary)
print("Annual Bonus:", bonus)
print("Total Annual Income:", total_income)
