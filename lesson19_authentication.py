"""
Lesson 19: Authentication - Password Hashing & Login

Demonstrates secure password storage using bcrypt hashing (never
storing plain-text passwords), with a register/login flow backed by
a real PostgreSQL database - users persist across restarts, unlike
an in-memory store. Also includes password strength validation, a
genuine production requirement.

Professionalization pass: upgraded from in-memory storage to real
PostgreSQL persistence, added password strength validation.
"""

import re

import bcrypt
import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

app = FastAPI()


def get_connection():
    """Create a new connection to the local PostgreSQL database."""
    return psycopg2.connect(dbname="mydb")


class UserCredentials(BaseModel):
    username: str
    password: str

    @field_validator("username")
    @classmethod
    def username_must_be_valid(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters")
        return value

    @field_validator("password")
    @classmethod
    def password_must_be_strong(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[0-9]", value):
            raise ValueError("Password must contain at least one number")
        return value


@app.post("/register")
def register(credentials: UserCredentials):
    """Register a new user, storing only a bcrypt hash in PostgreSQL."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = %s", (credentials.username,))
    if cursor.fetchone() is not None:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = bcrypt.hashpw(credentials.password.encode(), bcrypt.gensalt())
    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
        (credentials.username, hashed_password),
    )
    conn.commit()
    cursor.close()
    conn.close()

    return {"message": f"User '{credentials.username}' registered successfully"}


@app.post("/login")
def login(credentials: UserCredentials):
    """Verify login credentials against the bcrypt hash stored in PostgreSQL."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = %s", (credentials.username,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    stored_hash = bytes(row[0])
    if not bcrypt.checkpw(credentials.password.encode(), stored_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": f"Welcome back, {credentials.username}!"}
