from requests import Session

from ..models import Book
from .settings import get_settings


class PybraryApiClient:
    def __init__(self):
        self.settings = get_settings()
        self.url = str(self.settings.api_url)
        self.session = Session()

    def get_book(self, book_id: int) -> Book:
        url = f"{self.url}/books/{book_id}"
        response = self.session.get(url)
        response.raise_for_status()
        return Book.model_validate(response.json())
