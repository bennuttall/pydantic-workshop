from ..models import Book
from .settings import get_settings


settings = get_settings()


def get_book(book_id: int) -> Book:
    book_path = settings.books_dir / f"{book_id}.json"
    return Book.model_validate_json(book_path.read_text())
