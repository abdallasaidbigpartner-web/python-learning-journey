"""
Lesson 13: Type Hints

Demonstrates adding type hints to function parameters, return
values, and variables - professional practice that documents
intent and helps tooling catch bugs early.
"""

from typing import List, Dict

def calculate_average(scores: List[int]) -> float:
    return sum(scores) / len(scores)

def get_top_student(students: Dict[str, int]) -> str:
    return max(students, key=students.get)

test_scores: List[int] = [80, 90, 70, 100]
student_grades: Dict[str, int] = {"Sara": 90, "Abdalla": 95, "Cawad": 85}

average: float = calculate_average(test_scores)
top_student: str = get_top_student(student_grades)

print(average)
print(top_student)
