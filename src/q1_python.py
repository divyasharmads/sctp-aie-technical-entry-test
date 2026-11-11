# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Task 1:
# Write a function called convertTemp that accepts two arguments:
#   - value: a numeric temperature value
#   - unit: a string, either "C" for Celsius or "F" for Fahrenheit
#
# The function should:
#   - Convert Celsius to Fahrenheit if unit is "C"  →  Formula: (value × 9/5) + 32
#   - Convert Fahrenheit to Celsius if unit is "F"  →  Formula: (value − 32) × 5/9
#   - Return -1 if unit is neither "C" nor "F"
#   - Round the result to 2 decimal places before returning

def convertTemp(value, unit):
    if unit == "C":
        return round((value * 9/5) + 32, 2)
    elif unit == "F":
        return round((value - 32) * 5/9, 2)
    else:
        return -1


print(convertTemp(100, "C"))
print(convertTemp(32, "F"))
print(convertTemp(37, "C"))
print(convertTemp("invalid", "X"))
