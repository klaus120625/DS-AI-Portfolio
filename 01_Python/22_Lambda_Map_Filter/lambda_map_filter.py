
# Program 1: Lambda Function

# Normal function
def square(number):
    return number ** 2


# Lambda function
square_lambda = lambda number: number ** 2

print("Normal function:", square(5))
print("Lambda function:", square_lambda(5))

# Practical example: calculate prices with tax
calculate_price = lambda price: price * 1.18

print("Price with 18% tax:", calculate_price(1000))



# Program 2: Using map()

numbers = [1, 2, 3, 4, 5, 6]

# Apply the lambda function to every number
squares = list(map(lambda number: number ** 2, numbers))

print("Original numbers:", numbers)
print("Squared numbers:", squares)

# Practical example: convert prices from dollars to rupees
prices_usd = [10, 20, 30, 40]
exchange_rate = 83

prices_inr = list(
    map(lambda price: price * exchange_rate, prices_usd)
)

print("Prices in INR:", prices_inr)


# Program 3: Using filter()

scores = [32, 45, 58, 67, 39, 81, 92, 48, 76]

# Keep scores greater than or equal to 50
passing_scores = list(
    filter(lambda score: score >= 50, scores)
)

print("All scores:", scores)
print("Passing scores:", passing_scores)

# Practical example: filter high-performing ML models
accuracies = [72.5, 88.0, 91.5, 67.0, 95.2, 84.5]

high_accuracy = list(
    filter(lambda accuracy: accuracy >= 90, accuracies)
)

print("High-accuracy models:", high_accuracy)

