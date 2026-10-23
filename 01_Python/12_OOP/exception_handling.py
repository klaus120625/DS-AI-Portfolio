# Exception Handling
# Handling Division by Zero

try:
    numerator = 100
    denominator = 0

    result = numerator / denominator

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

print("Program continues running.")


# Exception Handling
# Handling Specific Errors

try:
    age = int("abc")
    print("Age:", age)

except ValueError:
    print("Error: Please provide a valid number.")

except TypeError:
    print("Error: Unexpected data type.")

print("Program completed successfully.")



# Exception Handling
# Practical Data Cleaning

raw_values = ["100", "250", "abc", "400", "", "150"]

clean_values = []
invalid_values = []

for value in raw_values:
    try:
        number = float(value)
        clean_values.append(number)

    except ValueError:
        invalid_values.append(value)

print("Original Values:", raw_values)
print("Clean Values:", clean_values)
print("Invalid Values:", invalid_values)

if clean_values:
    average = sum(clean_values) / len(clean_values)
    print("Average:", average)