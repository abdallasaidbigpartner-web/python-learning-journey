"""
Lesson 11: File Handling

Demonstrates writing to a file, appending additional content, and
reading it back both as a whole and line-by-line - core I/O skills
needed for any real program that persists data.
"""

with open("journal.txt", "w") as file:
    file.write("Day 1: Started learning Python.\n")
    file.write("Day 2: Learned about classes.\n")

with open("journal.txt", "a") as file:
    file.write("Day 3: Learned about file handling.\n")

print("Full file content:")
with open("journal.txt", "r") as file:
    print(file.read())

print("Reading line by line:")
with open("journal.txt", "r") as file:
    for line in file:
        print("-", line.strip())
