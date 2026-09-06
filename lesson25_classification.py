"""
Lesson 25: Classification - Predicting Categories

Demonstrates binary classification with Logistic Regression: using
two features (hours studied, previous score) to predict a pass/fail
outcome, then evaluating accuracy.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features: [hours_studied, previous_score]
X = np.array([
    [1, 40], [2, 45], [3, 55], [4, 60],
    [5, 70], [6, 75], [7, 85], [8, 90]
])
# Labels: 0 = fail, 1 = pass
y = np.array([0, 0, 0, 1, 1, 1, 1, 1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual:", y_test)
print("Predicted:", predictions)

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.1f}%")

new_student = [[5.5, 65]]
result = model.predict(new_student)
print(f"Prediction for 5.5 hours, previous score 65: {'Pass' if result[0] == 1 else 'Fail'}")
