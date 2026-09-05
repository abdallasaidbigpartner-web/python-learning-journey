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
