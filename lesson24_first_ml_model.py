"""
Lesson 24: Your First Machine Learning Model (Linear Regression)

Demonstrates the full basic ML workflow: preparing data, splitting
into train/test sets, training a Linear Regression model, making
predictions, and evaluating accuracy with mean absolute error.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
exam_scores = np.array([50, 55, 65, 70, 75, 85, 90, 95])

X_train, X_test, y_train, y_test = train_test_split(
    hours_studied, exam_scores, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual scores:", y_test)
print("Predicted scores:", predictions)

mae = mean_absolute_error(y_test, predictions)
print(f"Average prediction error: {mae:.2f}")

new_prediction = model.predict([[9]])
print(f"Predicted score for 9 hours studied: {new_prediction[0]:.2f}")
