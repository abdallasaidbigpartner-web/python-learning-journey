"""
Lesson 18: Connecting the API to a Real Database

Demonstrates replacing hardcoded/fake data with real queries against
a PostgreSQL database, using psycopg2 - a professional-grade Python
database driver.
"""

from fastapi import FastAPI, HTTPException
import psycopg2

app = FastAPI()


def get_connection():
    """Create a new connection to the local PostgreSQL database."""
    return psycopg2.connect(dbname="mydb")


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
