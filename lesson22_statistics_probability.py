"""
Lesson 22: Statistics & Probability Basics

Demonstrates mean, median, standard deviation, and variance using
NumPy, plus a basic probability simulation (coin flips) illustrating
the Law of Large Numbers - foundational concepts for understanding
how machine learning models measure and use data.
"""

import numpy as np
import random

test_scores = np.array([65, 70, 75, 80, 85, 90, 95, 100])

print("Mean:", np.mean(test_scores))
print("Median:", np.median(test_scores))
print("Standard deviation:", np.std(test_scores))
print("Variance:", np.var(test_scores))

flips = [random.choice(["Heads", "Tails"]) for _ in range(10000)]
heads_count = flips.count("Heads")
probability_heads = heads_count / len(flips)

print(f"Probability of heads (10000 flips): {probability_heads}")
