from typing import List

from services.books_service import Book


class Library:
    DAYS_TO_RETURN: int = 7

    def __init__(self):
        self._books: List[Book] = []

    def __repr__(self):
        return "\n".join(str(book) for book in self._books)

    def add_book(self, book: Book) -> Book:
        self._books.append(book)
        return book

    def borrow_book(self, requested_book: Book):
        for book in self._books:
            if requested_book == book and book.is_available():
                book.set_unavailable()
                book.set_return_date(self.DAYS_TO_RETURN)
                print("Book borrowed successfully.")
                return
        print("Book not available.")

    def return_book(self, requested_book: Book):
        for book in self._books:
            if requested_book == book and book.is_unavailable():
                book.set_available()
                book.set_return_date(None)
                print("Book returned successfully.")
                return
        print("Book was not borrowed.")

    def search_books(self, text: str) -> List[Book]:
        found_books = []
        for book in self._books:
            if (book.author == text or book.name == text) and book not in found_books:
                found_books.append(book)
        return sorted(found_books, key=lambda x: x.year, reverse=True)

    @property
    def books(self) -> List[Book]:
        """Read-only access to the book list."""
        return list(self._books)
