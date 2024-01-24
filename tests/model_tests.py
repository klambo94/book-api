import unittest

from src.models import Book, Author, Session


class MyTestCase(unittest.TestCase):
    def test_book_and_author_model_creation(self):
        author_model = Author(firstname="John", lastname="Goodman")
        Session.add(author_model)
        Session.commit()

        authors = Session.query(Author).filter_by(firstname="John", lastname="Goodman").all()
        author_id = authors[0].id
        book_model = Book(isbn="123", name="numbers", author_id=author_id)
        Session.add(book_model)
        Session.commit()

        books = Session.query(Book).all()
        authors = Session.query(Author).all()

        print(books.__str__())
        print(authors.__str__())

        assert len(books) == 1
        assert len(authors) == 1







if __name__ == '__main__':
    unittest.main()
