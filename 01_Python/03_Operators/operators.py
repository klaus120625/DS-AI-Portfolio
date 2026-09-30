# Python Operators

a = 10
b = 3

print("Arithmetic Operators:")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

print("\nComparison Operators:")

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\nLogical Operators:")

x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\nAssignment Operators:")

number = 10

print("Initial value:", number)

number += 5
print("After += 5:", number)

number -= 3
print("After -= 3:", number)

number *= 2
print("After *= 2:", number)

number /= 4
print("After /= 4:", number)

print("\nMembership Operators:")

fruits = ["apple", "banana", "mango", "orange"]

print("'apple' in fruits:", "apple" in fruits)
print("'grapes' in fruits:", "grapes" in fruits)
print("'grapes' not in fruits:", "grapes" not in fruits)

print("\nIdentity Operators:")

list1 = ["Python", "SQL", "AI"]
list2 = list1
list3 = ["Python", "SQL", "AI"]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)


print("\nBitwise Operators:")

a = 5
b = 3

print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)