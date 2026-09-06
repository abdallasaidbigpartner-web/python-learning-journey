"""
Professionalization pass: automated test for Lesson 26's overfitting
demonstration.

Verifies the core claim of the lesson programmatically: an
unrestricted Decision Tree should show a larger gap between training
and test accuracy (evidence of overfitting) than a depth-limited one.
"""

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def test_unrestricted_tree_overfits_more_than_limited_tree():
    np.random.seed(42)

    hours = np.random.uniform(0, 10, 100)
    previous_scores = np.random.uniform(30, 100, 100)
    X = np.column_stack([hours, previous_scores])

    y = ((hours * 5 + previous_scores) > 70).astype(int)
    noise = np.random.choice([0, 1], size=100, p=[0.9, 0.1])
    y = np.where(noise == 1, 1 - y, y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    overfit_model = DecisionTreeClassifier(random_state=42)
    overfit_model.fit(X_train, y_train)
    overfit_train_acc = accuracy_score(y_train, overfit_model.predict(X_train))
    overfit_test_acc = accuracy_score(y_test, overfit_model.predict(X_test))
    overfit_gap = overfit_train_acc - overfit_test_acc

    limited_model = DecisionTreeClassifier(max_depth=3, random_state=42)
    limited_model.fit(X_train, y_train)
    limited_train_acc = accuracy_score(y_train, limited_model.predict(X_train))
    limited_test_acc = accuracy_score(y_test, limited_model.predict(X_test))
    limited_gap = limited_train_acc - limited_test_acc

    assert overfit_train_acc >= limited_train_acc, "Unrestricted tree should fit training data at least as well"
    assert overfit_gap >= limited_gap, (
        f"Expected unrestricted tree's train/test gap ({overfit_gap:.3f}) "
        f"to be >= limited tree's gap ({limited_gap:.3f})"
    )
