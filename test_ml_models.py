"""
Professionalization pass: automated tests for Lesson 24 (Linear
Regression) and Lesson 25 (Logistic Regression) models.

Demonstrates testing ML code - not just "does it run," but "does the
model actually learn a sensible pattern." This is standard practice
in real ML engineering: models need regression tests just like any
other code, to catch silent degradation if data or code changes.
"""

import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression


def test_linear_regression_learns_positive_trend():
    """More hours studied should predict a higher score."""
    hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
    scores = np.array([50, 55, 65, 70, 75, 85, 90, 95])

    model = LinearRegression()
    model.fit(hours, scores)

    low_prediction = model.predict([[1]])[0]
    high_prediction = model.predict([[8]])[0]

    assert high_prediction > low_prediction, "More study hours should predict a higher score"


def test_linear_regression_reasonable_accuracy():
    """The model's predictions should be close to actual training values."""
    hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
    scores = np.array([50, 55, 65, 70, 75, 85, 90, 95])

    model = LinearRegression()
    model.fit(hours, scores)
    predictions = model.predict(hours)

    mean_error = np.mean(np.abs(predictions - scores))
    assert mean_error < 5, f"Model error too high: {mean_error}"


def test_logistic_regression_classifies_correctly():
    """Clear pass/fail cases should be classified correctly."""
    X = np.array([[1, 40], [2, 45], [3, 55], [4, 60], [5, 70], [6, 75], [7, 85], [8, 90]])
    y = np.array([0, 0, 0, 1, 1, 1, 1, 1])

    model = LogisticRegression()
    model.fit(X, y)

    clear_fail = model.predict([[1, 35]])[0]
    clear_pass = model.predict([[8, 95]])[0]

    assert clear_fail == 0, "Low hours/score should predict fail"
    assert clear_pass == 1, "High hours/score should predict pass"
