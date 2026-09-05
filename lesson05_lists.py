"""
Lesson 5: Lists

Demonstrates list creation, indexing (including negative indexing),
append, remove, and using len() to get list size.
"""

colors = ["red", "blue", "green", "yellow"]

print(colors[0])
print(colors[-1])

colors.append("purple")
colors.remove("blue")

print(colors)
print(len(colors))
