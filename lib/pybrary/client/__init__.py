import requests

from ..models import Book
from .settings import get_settings


class ApiClient:
    def __init__(self):
        self.settings = get_settings()

    def get_book(self, book_id: int) -> Book:
        response = requests.get(f"{self.base_url}/books/{book_id}")
        response.raise_for_status()
        return Book.model_validate(response.json())
