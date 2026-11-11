# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

def formatName(firstName, lastName):
    return f"{lastName.capitalize()}, {firstName.capitalize()}"

def formatInitials(firstName, lastName):
    return f"{firstName[0].upper()}.{lastName[0].upper()}."

print(formatName("Alice", "Tan"))
print(formatName("bob", "lim"))
print(formatInitials("Alice", "Tan"))
print(formatInitials("bob", "lim"))
