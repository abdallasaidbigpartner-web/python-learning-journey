"""
Lesson 7: Tuples & Sets

Demonstrates tuples (immutable ordered data, e.g. coordinates) and
sets (unordered unique values) - including adding, removing, and
using sets to eliminate duplicates from a list.
"""

coordinates = (35, 15)
print(coordinates[0])
print(coordinates[1])

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

unique_numbers.add(10)
unique_numbers.remove(1)
print(unique_numbers)
