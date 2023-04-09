import unittest
from models.book import Book

class TestBook(unittest.TestCase):

    def SetUp(self):

        book_1 = Book(1, "The Magic mountain", "Thomas Mann", "Classic Literature", True)
        book_2 = Book(2, "Pet Semetary", "Stephen King", "Horror", False)
        book_3 = Book(3, "Anna Karenina", "Leo Tolstoy", "Romance", True)

        books = [book_1, book_2, book_3]

    def test_book_has_id(self):
        self.assertEqual(1, self.book_1.id)
    
    def test_book_has_title(self):
        self.assertEqual("The Magic Mountain", self.book_1.title)

    def test_book_has_author(self):
        self.assertEqual("Thomas Mann", self.book_1.author)

    def test_book_has_genre(self):
        self.assertEqual("Classic Literature", self.book_1.genre)

    def test_book_is_checked_out(self):
        self.assertEqual(True, self.book_1.checked_out)

