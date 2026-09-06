"""
Lesson 17: Building Your First API (FastAPI)

Demonstrates creating a basic HTTP API with GET and POST endpoints,
using FastAPI - a modern, professional-grade Python web framework
used throughout the industry.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Root endpoint - simple health check."""
    return {"message": "API is running"}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    """Return a fake student record by ID."""
    return {"id": student_id, "name": "Abdalla", "grade": "A"}


@app.post("/students")
def create_student(name: str, age: int):
    """Create a new student (in-memory example, no real database yet)."""
    return {"message": f"Student {name}, age {age}, created successfully"}
