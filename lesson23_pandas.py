"""
Lesson 23: pandas - Working With Real Datasets

Demonstrates loading a CSV into a DataFrame, exploring it with
head()/describe(), filtering rows, sorting, and computing column
statistics - core data analysis skills used before any ML modeling.
"""

import pandas as pd

df = pd.read_csv("students.csv")

print("First rows:")
print(df.head())

print("\nStatistics:")
print(df.describe())

print("\nAverage score:", df["score"].mean())

print("\nStudents with score >= 85:")
print(df[df["score"] >= 85])

print("\nSorted by score (descending):")
print(df.sort_values("score", ascending=False))
