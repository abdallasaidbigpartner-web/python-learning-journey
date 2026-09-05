"""
Practice: Tuples & Dictionaries in Loops

Demonstrates unpacking tuples and dictionary items correctly in a
for loop, with variable names matching the real data order.
"""

fruits = [(1, "apple"), (3, "banana"), (1000, "cherry")]

for quantity, fruit in fruits:
    print(quantity, fruit)

fruits_dict = {"apple": 1, "banana": 3, "cherry": 1000}

for fruit, quantity in fruits_dict.items():
    print(quantity, fruit)

