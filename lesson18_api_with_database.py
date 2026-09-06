"""
Lesson 18: Connecting the API to a Real Database

Demonstrates a full CRUD-capable API backed by PostgreSQL, using
psycopg2 - a professional-grade Python database driver. Includes
input validation via Pydantic to reject malformed requests before
they ever reach the database.

Professionalization pass: added POST /students to actually create
records (previously read-only), with Pydantic validation on grade
values and student age.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import psycopg2

app = FastAPI()

VALID_GRADES = ["A", "B", "C", "D", "F"]


def get_connection():
    """Create a new connection to the local PostgreSQL database."""
    return psycopg2.connect(dbname="mydb")


class NewStudent(BaseModel):
    name: str
    age: int
    grade: str

    @field_validator("age")
    @classmethod
    def age_must_be_reasonable(cls, value: int) -> int:
        if value <= 0 or value > 120:
            raise ValueError("Age must be between 1 and 120")
        return value

    @field_validator("grade")
    @classmethod
    def grade_must_be_valid(cls, value: str) -> str:
        if value not in VALID_GRADES:
            raise ValueError(f"Grade must be one of {VALID_GRADES}")
        return value


@app.get("/")
def read_root():
    return {"message": "API connected to real database"}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    """Fetch a real student from the database by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, grade FROM students WHERE id = %s", (student_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"id": row[0], "name": row[1], "age": row[2], "grade": row[3]}


@app.get("/students")
def get_all_students():
    """Fetch all real students from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, grade FROM students")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [{"id": r[0], "name": r[1], "age": r[2], "grade": r[3]} for r in rows]


@app.post("/students")
def create_student(student: NewStudent):
    """Create a new student record in the real database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s) RETURNING id",
        (student.name, student.age, student.grade),
    )
    new_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()

    return {"id": new_id, "name": student.name, "age": student.age, "grade": student.grade}
