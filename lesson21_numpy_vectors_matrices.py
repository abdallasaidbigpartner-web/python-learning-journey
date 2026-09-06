"""
Lesson 21: Vectors, Matrices & NumPy

Demonstrates creating vectors and matrices with NumPy, element-wise
operations, the dot product, and matrix multiplication - the core
mathematical operations underlying all machine learning.
"""

import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

print("Vector addition:", vector_a + vector_b)
print("Element-wise multiplication:", vector_a * vector_b)
print("Dot product:", np.dot(vector_a, vector_b))

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("Matrix shape:", matrix1.shape)
print("Matrix multiplication:")
print(np.matmul(matrix1, matrix2))
