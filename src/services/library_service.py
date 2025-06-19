from typing import List

from src.services.books_service import Book


class Library:
    def __init__(self):
        self._books: List[Book] = []

    def __repr__(self) -> str:
        return "\n".join(str(book) for book in self._books)

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def borrow_book(self, requested_book: Book) -> bool:
        """Attempts to borrow a book. Returns True if successful."""
        for book in self._books:
            if book == requested_book and book.is_available():
                book.set_unavailable()
                return True
        return False

    def return_book(self, requested_book: Book) -> bool:
        """Attempts to return a book. Returns True if successful."""
        for book in self._books:
            if book == requested_book and book.is_unavailable():
                book.set_available()
                return True
        return False

    def search_books(self, query: str) -> List[Book]:
        """Returns a list of books matching the title or author."""
        matched = [
            book for book in self._books
            if book.name == query or book.author == query
        ]
        return sorted(matched, key=lambda b: b.year, reverse=True)

    @property
    def books(self) -> List[Book]:
        """Read-only access to the book list."""
        return list(self._books)
