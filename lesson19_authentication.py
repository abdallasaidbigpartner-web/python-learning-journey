"""
Lesson 19: Authentication - Password Hashing & Login

Demonstrates secure password storage using bcrypt hashing (never
storing plain-text passwords), plus a simple register/login flow
using an in-memory user store.
"""

import bcrypt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory "database" for this lesson - a real app would use PostgreSQL
users_db: dict[str, bytes] = {}


class UserCredentials(BaseModel):
    username: str
    password: str


@app.post("/register")
def register(credentials: UserCredentials):
    """Register a new user, storing only a bcrypt hash of their password."""
    if credentials.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = bcrypt.hashpw(credentials.password.encode(), bcrypt.gensalt())
    users_db[credentials.username] = hashed_password

    return {"message": f"User '{credentials.username}' registered successfully"}


@app.post("/login")
def login(credentials: UserCredentials):
    """Verify login credentials against the stored bcrypt hash."""
    stored_hash = users_db.get(credentials.username)

    if stored_hash is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not bcrypt.checkpw(credentials.password.encode(), stored_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": f"Welcome back, {credentials.username}!"}
