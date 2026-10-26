
# Program 1: Basic List Comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number ** 2 for number in numbers]

print("Original numbers:", numbers)
print("Squares:", squares)



# Program 2: Filter Even Numbers

numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]

even_numbers = [
    number for number in numbers
    if number % 2 == 0
]

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)


# Program 3: Data Preprocessing

scores = [35, 42, 58, 67, 74, 81, 90, 28, 96]

# Keep passing scores (50 and above)
passing_scores = [
    score for score in scores
    if score >= 50
]

# Convert scores out of 100 into decimal proportions
score_proportions = [
    round(score / 100, 2)
    for score in passing_scores
]

print("Original scores:", scores)
print("Passing scores:", passing_scores)
print("Score proportions:", score_proportions)
