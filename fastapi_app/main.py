from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database  # Relative imports are OK now

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books/", response_model=list[schemas.Book])
def book_list(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.post("/books/", response_model=schemas.Book, status_code=201)
def book_create(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)
