"""
Lesson 26: Decision Trees & Overfitting

Demonstrates a Decision Tree classifier, and the critical concept of
overfitting - comparing an unrestricted tree (which memorizes
training data) against a depth-limited tree (which generalizes
better), using train vs test accuracy as the diagnostic signal.
"""

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)

# Simulate 100 students: [hours_studied, previous_score] -> pass/fail
hours = np.random.uniform(0, 10, 100)
previous_scores = np.random.uniform(30, 100, 100)
X = np.column_stack([hours, previous_scores])

# Pass if a rough combination crosses a threshold, plus some randomness (realistic noise)
y = ((hours * 5 + previous_scores) > 70).astype(int)
noise = np.random.choice([0, 1], size=100, p=[0.9, 0.1])
y = np.where(noise == 1, 1 - y, y)  # flip 10% of labels to simulate real-world noise

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("=== Unrestricted Tree (prone to overfitting) ===")
overfit_model = DecisionTreeClassifier(random_state=42)
overfit_model.fit(X_train, y_train)
print("Training accuracy:", accuracy_score(y_train, overfit_model.predict(X_train)))
print("Test accuracy:", accuracy_score(y_test, overfit_model.predict(X_test)))

print("\n=== Depth-Limited Tree (better generalization) ===")
limited_model = DecisionTreeClassifier(max_depth=3, random_state=42)
limited_model.fit(X_train, y_train)
print("Training accuracy:", accuracy_score(y_train, limited_model.predict(X_train)))
print("Test accuracy:", accuracy_score(y_test, limited_model.predict(X_test)))
