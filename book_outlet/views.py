from django.shortcuts import render, get_object_or_404
from .models import Book


def index(request):
    books = Book.objects.all().order_by("title")
    total_books = books.count()
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_number_of_books": total_books,
        },
    )


def book_detail(request, slug):
    book = Book.objects.filter(slug=slug).first()
    if not book:
        if slug.isdigit():
            book = get_object_or_404(Book, pk=int(slug))
        else:
            parts = slug.rsplit("-", 1)
            if len(parts) == 2 and parts[1].isdigit():
                book = get_object_or_404(Book, pk=int(parts[1]))
            else:
                book = get_object_or_404(Book, slug=slug)

    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "book": book,
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestselling": book.is_bestselling,
            "slug": book.slug,
        },
    )
