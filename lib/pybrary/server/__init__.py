from fastapi import FastAPI, HTTPException

from ..models import Book
from . import utils


app = FastAPI(title="Pybrary")


@app.get("/")
def index():
    return {"message": "Hello world"}


@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book:
    book = utils.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
