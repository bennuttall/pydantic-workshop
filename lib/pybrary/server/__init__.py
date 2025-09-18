from fastapi import FastAPI

from ..models import Book
from . import utils


app = FastAPI(title="Pybrary")


@app.get("/")
def index():
    return {"message": "Hello world"}


@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book:
    return utils.get_book(book_id)
