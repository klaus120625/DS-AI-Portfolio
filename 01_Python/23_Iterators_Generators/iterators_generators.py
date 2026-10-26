
#Program 1: Iterators

numbers = [10, 20, 30, 40, 50]

# Convert the list into an iterator
number_iterator = iter(numbers)

# Retrieve values one at a time
print("First value:", next(number_iterator))
print("Second value:", next(number_iterator))
print("Third value:", next(number_iterator))

print("Remaining values:")

for number in number_iterator:
    print(number)


# Program 2: Generator Function

def generate_numbers(limit):
    number = 1

    while number <= limit:
        yield number
        number += 1


# Create a generator object
numbers = generate_numbers(5)

print("Generated values:")

for value in numbers:
    print(value)

    
# Program 3: Generator for Data Processing

students = [
    {"name": "Alex", "score": 85},
    {"name": "Sam", "score": 42},
    {"name": "Jordan", "score": 91},
    {"name": "Taylor", "score": 67},
    {"name": "Morgan", "score": 38}
]


def high_scoring_students(records, threshold):
    for student in records:
        if student["score"] >= threshold:
            yield student


# Get passing students one at a time
results = high_scoring_students(students, 60)

print("Students scoring 60 or above:")

for student in results:
    print(student["name"], "-", student["score"])

