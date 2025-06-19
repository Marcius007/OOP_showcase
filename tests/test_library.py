import unittest

from src.services.books_service import BookStatus
from src.services.library_service import Book, Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book("Book One", "Author A", 2001)
        self.book2 = Book("Book One", "Author A", 2001)  # same as book1
        self.book3 = Book("Book Two", "Author B", 2005)

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.assertIn(self.book1, self.library.books)

    def test_get_book_available(self):
        self.library.add_book(self.book1)
        self.library.get_book(self.book2)  # same details as book1
        self.assertEqual(self.library.books[0].status, BookStatus.UNAVAILABLE)

    def test_get_book_unavailable(self):
        self.library.add_book(self.book1)
        self.library.get_book(self.book2)
        self.library.get_book(self.book2)  # second time, should not find available
        self.assertEqual(self.library.books[0].status, BookStatus.UNAVAILABLE)

    def test_return_book(self):
        self.library.add_book(self.book1)
        self.library.get_book(self.book1)
        self.library.return_book(self.book1)
        self.assertEqual(self.library.books[0].status, BookStatus.AVAILABLE)

    def test_search_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book3)
        results = self.library.get_book_by_search("Book One")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Book One")


if __name__ == "__main__":
    unittest.main()
