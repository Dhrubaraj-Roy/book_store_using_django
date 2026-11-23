from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "rating", "is_bestselling")


admin.site.register(Book, BookAdmin)
