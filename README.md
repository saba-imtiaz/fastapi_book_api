# 📚 FastAPI Book API

A simple **Book Management API** built with **FastAPI** and **SQLAlchemy**.
This project allows you to create and list books using a SQLite database.

## 🚀 Features

* Add new books (`POST /books/`)
* Retrieve all books (`GET /books/`)
* Uses **FastAPI** for quick API development
* Uses **SQLAlchemy ORM** with SQLite
* Data validation with **Pydantic**

## 📂 Project Structure

```
fastapi_book_api/
│── fastapi_app/
│   │── main.py          # FastAPI application entry point
│   │── models.py        # SQLAlchemy models (Book table)
│   │── schemas.py       # Pydantic schemas for request/response
│   │── crud.py          # Database operations (CRUD functions)
│   │── database.py      # Database engine & session
│   │── __init__.py
│── .venv/               # Virtual environment

## ⚙️ Installation & Setup

### 1. Clone the repository


git clone https://github.com/your-username/fastapi_book_api.git
cd fastapi_book_api

### 2. Create and activate a virtual environment

python -m venv .venv
.venv\Scripts\activate   # On Windows
source .venv/bin/activate  # On Mac/Linux

### 3. Install dependencies

pip install fastapi uvicorn sqlalchemy pydantic

### 4. Run the server

uvicorn fastapi_app.main:app --reload

## 📖 API Endpoints

### 1. List all books

**Request**

```http
GET /books/
```

**Response**

```json
[
  {
    "id": 1,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "published_year": 2008
  }
]

### 2. Create a new book

**Request**

```http
POST /books/
```

**Body**

```json
{
  "title": "The Pragmatic Programmer",
  "author": "Andrew Hunt",
  "published_year": 1999
}
```

**Response**

```json
{
  "id": 2,
  "title": "The Pragmatic Programmer",
  "author": "Andrew Hunt",
  "published_year": 1999
}


## 📑 API Docs

FastAPI automatically provides interactive API docs:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🛠️ Tech Stack

* **FastAPI** (Web framework)
* **SQLAlchemy** (ORM for database)
* **SQLite** (Lightweight database)
* **Pydantic** (Data validation)

