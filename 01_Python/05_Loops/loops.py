# Python Loops

# Example 1: For loop

for i in range(1, 6):
    print(i)

    # Example 2: for loop with a list

subjects = ["Python", "SQL", "Statistics", "Machine Learning"]

for subject in subjects:
    print(subject)


    # Example 3: for loop with range

for i in range(5):
    print(i)


for i in range(2, 7):
    print(i)

for i in range(2, 11, 2):
    print(i)

# Example 3: while loop

count = 1

while count <= 5:
    print(count)
    count += 1

# Example 4: break statement

for i in range(1, 11):
    if i == 6:
        break ## Break condition/statement
    print(i)

 ## continue statement skips the current iteration and moves to the next iteration of the loop.

# Example 5: continue statement

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

## break     → STOP the entire loop , continue  → SKIP this iteration.

## PASS is a placeholder statement. It tells Python:

## “Do nothing here for now.”

## It's useful when you're creating a program structure but haven't written the logic yet.

# Example 6: pass statement

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

    ##break     → stops the loop.
    ##continue  → skips the current iteration.
    ##pass      → does nothing.

## Nested Loops

## A nested loop means putting one loop inside another loop.

# Example 7: Nested loops

for i in range(1, 4):
    for j in range(1, 4):
        print("i =", i, "j =", j)


## Practical Example: calculate the average of a small dataset using a for loop.

marks = [80, 75, 90, 85, 70]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("\nStudent Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)