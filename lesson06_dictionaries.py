"""
Lesson 6: Dictionaries

Demonstrates key-value data storage: accessing, updating, and adding
keys, looping with .items(), and checking key existence with "in".
"""

# Lesson 6: Dictionaries

student = {"name": "Abdalla", "age": 33, "grade": "A"}

print(student["name"])
print(student["grade"])

student["age"] = 21
student["school"] = "Al-Hikma"

for key, value in student.items():
    print(key, ":", value)

if "grade" in student:
    print("Grade is listed")
