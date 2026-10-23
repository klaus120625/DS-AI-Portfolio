# File Handling
# Write Data to a File

with open("student.txt", "w") as file:
    file.write("Name: Swarup\n")
    file.write("Course: Data Science and AI\n")
    file.write("Status: Learning Python")

print("Data written successfully!")



#  Read Data from a File

with open("student.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)



#File Handling
#File Analysis with Exception Handling

filename = "student.txt"

try:
    with open(filename, "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()

    print("File Name:", filename)
    print("Total Lines:", len(lines))
    print("Total Words:", len(words))
    print("Total Characters:", len(content))

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: Permission denied!")


#File Handling
#Read a File Line by Line

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())


#File Handling
#Append Data to a File

with open("student.txt", "a") as file:
    file.write("\nSkill: Python Programming")
    file.write("\nGoal: Become an AI Engineer")

print("New data appended successfully!")        


# File Handling
# File Analysis with Exception Handling

filename = "student.txt"

try:
    with open(filename, "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()

    print("File Name:", filename)
    print("Total Lines:", len(lines))
    print("Total Words:", len(words))
    print("Total Characters:", len(content))

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")