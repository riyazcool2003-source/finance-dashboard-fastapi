# Finance Dashboard Backend

Backend API for managing financial records with role-based access control.

---

## Tech Stack

- FastAPI
- SQLAlchemy ORM
- PostgreSQL / SQLite
- JWT Authentication
- Pydantic Validation

---

## Features

- User signup & login
- Role-based access control
- Transaction CRUD operations
- Dashboard summary analytics
- Input validation
- Production-ready structure
- CORS enabled

---

## Roles

### viewer
- can view transactions
- can view dashboard summary

### analyst
- can create transactions
- can update transactions
- can view dashboard summary

### admin
- full access
- can delete transactions
- can view all users

---

## API Endpoints

### Auth

POST /signup

POST /login

---

### Transactions

POST /transactions

GET /transactions

PUT /transactions/{id}

DELETE /transactions/{id}

---

### Dashboard

GET /dashboard/summary

---

### Admin

GET /admin/users

---

## Setup Instructions

Install dependencies

pip install -r requirements.txt


Run server

uvicorn app.main:app --reload


Open Swagger UI

http://127.0.0.1:8000/docs

---

## Example Roles

viewer

analyst

admin

---

## Database

Configured using SQLAlchemy ORM.

Environment variables stored in .env file.

---

## Project Goal

Demonstrates backend architecture, API design, role-based access control, and financial data processing.