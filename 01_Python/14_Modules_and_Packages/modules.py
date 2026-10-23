# Modules and Packages
# Using Built-in Modules

import math
import random
import datetime

number = 25

print("Square root:", math.sqrt(number))
print("Power:", math.pow(5, 2))
print("Random number:", random.randint(1, 100))
print("Today's date:", datetime.date.today())

# Day 14 - Modules and Packages
# Code 3: Student Marks Analysis Using a Module

import statistics

marks = [78, 85, 92, 67, 88, 85, 90]

average_marks = statistics.mean(marks)
median_marks = statistics.median(marks)
most_common_marks = statistics.mode(marks)
standard_deviation = statistics.stdev(marks)

print("Student Marks:", marks)
print("Average Marks:", average_marks)
print("Median Marks:", median_marks)
print("Most Common Marks:", most_common_marks)
print("Standard Deviation:", round(standard_deviation, 2))