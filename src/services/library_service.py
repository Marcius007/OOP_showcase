from typing import List

from src.services.books_service import Book


class Library:

    def __init__(self):
        self.books: List[Book] = []

    def __repr__(self):
        return "\n".join(str(book) for book in self.books)

    def add_book(self, book: Book) -> Book:
        self.books.append(book)
        return book

    def get_book(self, requested_book: Book):
        for book in self.books:
            if requested_book == book and book.is_available():
                book.set_unavailable()
                print("Book borrowed successfully.")
                return
        print("Book not available.")

    def return_book(self, requested_book: Book):
        for book in self.books:
            if requested_book == book and book.is_unavailable():
                book.set_available()
                print("Book returned successfully.")
                return
        print("Book was not borrowed.")

    def get_book_by_search(self, text: str) -> List[Book]:
        found_books = []
        for book in self.books:
            if (book.author == text or book.name == text) and book not in found_books:
                found_books.append(book)
        return sorted(found_books, key=lambda x: x.year, reverse=True)
