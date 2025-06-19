from services.books_service import Book, BookStatus
from services.library_service import Library

library = Library()

def prompt_book() -> Book:
    name = input("Enter book name: ").strip()
    author = input("Enter author name: ").strip()
    year = int(input("Enter year: ").strip())
    return Book(name, author, year)

while True:
    print("\nOptions: add | get | return | search | list | quit")
    command = input("Choose an action: ").strip().lower()

    if command == "add":
        book = prompt_book()
        library.add_book(book)
        print("Book added.")

    elif command == "get":
        book = prompt_book()
        library.borrow_book(book)

    elif command == "return":
        book = prompt_book()
        book.status = BookStatus.UNAVAILABLE
        library.return_book(book)

    elif command == "search":
        text = input("Enter book title or author: ").strip()
        results = library.search_books(text)
        if results:
            print("Found books:")
            for b in results:
                print(b)
        else:
            print("No books found.")

    elif command == "list":
        print("Library contents:")
        print(library)

    elif command == "quit":
        print("Goodbye!")
        break

    else:
        print("Invalid command.")