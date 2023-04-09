from models.book import *

book_1 = Book(1, "The Magic mountain", "Thomas Mann", "Classic Literature", True)
book_2 = Book(2, "Pet Semetary", "Stephen King", "Horror", False)
book_3 = Book(3, "Anna Karenina", "Leo Tolstoy", "Romance", True)

books = [book_1, book_2, book_3]

def add_new_book(book):
    books.append(book)

def delete_book(book_name):
    book_to_remove = None
    for book in books:
        if book.title == book_name:
            book_to_remove = book
            break

    books.remove(book_to_remove)

