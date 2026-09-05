"""
Lesson 1: Variables & Basic Data Types

Demonstrates Python core types (str, int, float, bool) and f-strings
for formatted output - the foundation for all further Python work.
"""

first_name = "Cawad"
age = 40
height = 1.75
is_active = True

print("Hello {first_name}")     # missing f — what happens?
print(f"Hello {first_name}")    # correct

print(f"{first_name} is {age} years old and {height}m tall.")

temperature = 15

if temperature > 30:
    print("Hot")
elif temperature > 15 and temperature < 30:
    print("Warm")
else:
    print("Cold")

