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


@app.post("/books/")
def create_book(book: Book) -> Book:
    return utils.add_book(book)


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book) -> Book:
    updated_book = utils.update_book(book_id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    success = utils.delete_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
