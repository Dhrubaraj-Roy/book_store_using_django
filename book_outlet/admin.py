from django.contrib import admin
from .models import Book, Author, Address


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating", "is_bestselling")
    list_display = ("title", "author", "rating", "is_bestselling", "slug")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "address")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("city", "postal_code", "country")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
