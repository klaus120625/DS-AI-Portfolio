#  Strings
# String Indexing and Slicing

name = "Swarup"

print("Name:", name)

print("First character:", name[0])
print("Last character:", name[-1])

print("First three characters:", name[0:3])
print("Full name:", name[:])

# String Methods

message = "  welcome to python programming  "

print("Original:", message)

print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title Case:", message.title())
print("Clean Text:", message.strip())

print("Number of characters:", len(message))
print("Position of Python:", message.find("python"))

#  Practical String Processing

name = "  Swarup Patil  "
email = "swarup.patil@gmail.com"

# Remove extra spaces
clean_name = name.strip()

# Convert name to uppercase
upper_name = clean_name.upper()

# Extract username from email
username = email.split("@")[0]

# Check whether email is from Gmail
is_gmail = email.endswith("@gmail.com")

print("Original Name:", name)
print("Clean Name:", clean_name)
print("Uppercase Name:", upper_name)
print("Email Username:", username)
print("Is Gmail:", is_gmail)

