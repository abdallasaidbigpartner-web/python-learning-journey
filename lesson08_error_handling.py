"""
Lesson 8: Error Handling (try/except)

Demonstrates catching runtime errors gracefully instead of crashing,
handling multiple error types, and using else/finally for cleanup
and confirmation logic.
"""

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
        return None
    else:
        print("Division succeeded")
        return result
    finally:
        print("Finished attempting division")

print(safe_divide(10, 2))
print(safe_divide(10, 0))

try:
    number = int("not_a_number")
except ValueError:
    print("Error: invalid number format")
