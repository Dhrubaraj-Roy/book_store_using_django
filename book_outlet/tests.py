from django.test import TestCase
from .models import Book, Author


class AuthorModelTest(TestCase):
    def test_author_str_and_full_name(self):
        author = Author.objects.create(first_name="J.K.", last_name="Rowling")
        self.assertEqual(author.full_name(), "J.K. Rowling")
        self.assertEqual(str(author), "J.K. Rowling")

    def test_book_foreign_key_relationship(self):
        author = Author.objects.create(first_name="George", last_name="Orwell")
        book = Book.objects.create(title="1984", rating=5, author=author)
        self.assertEqual(book.author, author)
        self.assertIn(book, author.book_set.all())

    def test_author_cascade_delete(self):
        author = Author.objects.create(first_name="J.R.R.", last_name="Tolkien")
        book = Book.objects.create(title="The Hobbit", rating=5, author=author)
        author_id = author.id
        book_id = book.id

        # Deleting the author should cascade and delete the book
        author.delete()
        self.assertFalse(Author.objects.filter(id=author_id).exists())
        self.assertFalse(Book.objects.filter(id=book_id).exists())

    def test_book_author_null_allowed(self):
        book = Book.objects.create(title="Anonymous Work", rating=3, author=None)
        self.assertIsNone(book.author)
        self.assertTrue(Book.objects.filter(id=book.id).exists())
