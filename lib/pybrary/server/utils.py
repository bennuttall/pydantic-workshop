from ..models import Book
from .settings import get_settings


settings = get_settings()


def get_book(book_id: int) -> Book | None:
    book_path = settings.books_dir / f"{book_id}.json"
    if not book_path.exists():
        return None
    return Book.model_validate_json(book_path.read_text())


def add_book(book: Book) -> Book:
    book_id = get_next_book_id()
    book_path = settings.books_dir / f"{book_id}.json"
    book_path.write_text(book.model_dump_json(indent=2))
    return book


def get_next_book_id() -> int:
    existing_ids = [int(p.stem) for p in settings.books_dir.glob("*.json") if p.stem.isdigit()]
    return max(existing_ids, default=0) + 1


def update_book(book_id: int, book: Book) -> Book | None:
    book_path = settings.books_dir / f"{book_id}.json"
    if not book_path.exists():
        return None
    book_path.write_text(book.model_dump_json(indent=2))
    return book


def delete_book(book_id: int) -> bool:
    book_path = settings.books_dir / f"{book_id}.json"
    if not book_path.exists():
        return False
    book_path.unlink()
    return True
