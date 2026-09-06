# Python Learning Journey



![Build Status](https://github.com/abdallasaidbigpartner-web/python-learning-journey/actions/workflows/docker-build.yml/badge.svg)



Structured Python engineering progression covering software development, backend APIs, databases, testing, Docker/CI, machine learning, and AI systems.

## Progress

### Python Fundamentals

- Lesson 1: Variables & data types
- Lesson 2: Conditionals (`if` / `elif` / `else`)
- Lesson 3: Loops (`for` / `while`)
- Lesson 4: Functions (parameters & return values)
- Lesson 5: Lists (indexing, appending, removing & slicing)
- Lesson 6: Dictionaries (key-value pairs)
- Lesson 7: Tuples & sets
- Lesson 8: Error handling (`try` / `except` / `else` / `finally`)
- Lesson 9: Classes, objects & inheritance
- Lesson 10: Modules & imports
- Lesson 11: File handling
- Lesson 12: JSON serialization
- Practice: Tuples & dictionaries in loops

### Software Engineering

- Lesson 13: Type hints
- Lesson 14: Automated testing with pytest
- Lesson 15: SOLID — Single Responsibility & Open/Closed Principles
- Lesson 16: SOLID — Liskov Substitution & Interface Segregation

### Backend Engineering

- Lesson 17: FastAPI — building HTTP APIs (with automated API tests via TestClient)
- Lesson 18: PostgreSQL — connecting an API to a real database, full CRUD with validation
- Lesson 19: Authentication — bcrypt password hashing, login, real PostgreSQL persistence

### DevOps & CI

- Lesson 20: Docker & GitHub Actions CI
- Dedicated, path-filtered CI workflows: Docker build, PyTorch tests (cloud), neural embedding tests (cloud), and a general test suite

### Machine Learning & Deep Learning

- Lesson 21: NumPy — vectors, matrices & matrix operations
- Lesson 22: Statistics & probability fundamentals
- Lesson 23: pandas — working with tabular datasets
- Lesson 24: Machine learning — linear regression (with automated model-behavior tests)
- Lesson 25: Machine learning — logistic regression classification (with automated tests)
- Lesson 26: Decision trees & overfitting (with automated tests verifying the overfitting gap)
- Lesson 27: Neural networks with PyTorch (tested via GitHub Actions cloud CI, since PyTorch cannot build on Android/Termux)

### Generative AI & Information Retrieval

- Lesson 28: LLM fundamentals — tokens, prompts & API calls (with mocked tests, avoiding real API calls in CI)
- Lesson 29: Classical text retrieval — TF-IDF & cosine similarity
- Lesson 30: Neural embeddings — semantic search with Sentence Transformers (cloud CI)
- Lesson 31: Retrieval-Augmented Generation (RAG) — combining retrieval with LLM grounding

### AI Agents

- Lesson 32: AI agents & tool calling — the LLM decides when to invoke a real function, executes it, and uses the result

### MLOps & Production

- Lesson 33: Serving a model in production — health checks, structured logging, model versioning, input validation

## Engineering Practices

- **Testing:** unit tests (pytest), API tests (FastAPI TestClient), mocked external-API tests, and cloud-CI-verified deep learning tests
- **CI/CD:** path-filtered GitHub Actions workflows so each pipeline only runs when relevant files change
- **Database-backed, not in-memory:** authentication and CRUD operations persist to real PostgreSQL
- **Input validation:** Pydantic validators reject malformed data before it reaches business logic

## Capstone Project

Skills from this repository (backend, database, auth, RAG) are combined into a single production-style system:
- [ai-study-assistant](https://github.com/abdallasaidbigpartner-web/ai-study-assistant) — FastAPI + PostgreSQL + bcrypt auth + RAG, with tests, Docker, and CI including a real ephemeral database service

## Related Repositories

- [typescript-learning-journey](https://github.com/abdallasaidbigpartner-web/typescript-learning-journey)
- [sql-learning-journey](https://github.com/abdallasaidbigpartner-web/sql-learning-journey)
