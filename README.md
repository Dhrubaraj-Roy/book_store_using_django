# Book Store Using Django

A Django project featuring the **`book_outlet`** application:
- **`book_outlet`**: Outlets catalog management, `Book`, `Author`, and `Address` models with relationships (One-to-One & Many-to-One), rating validators, automatic slug generation (`...harry-potter-id`), Django Admin integration, and responsive HTML templates.

---

## Features

- **Database Models & Relationships**:
  - `Address`: `city`, `postal_code`, and `country` with custom `verbose_name_plural = "Address Entries"`.
  - `Author`: `first_name`, `last_name`, helper method `full_name()`, and `address` (`models.OneToOneField(Address, on_delete=models.CASCADE, null=True)`).
  - `Book`: `title`, `rating` (1–5 scale with `MinValueValidator` and `MaxValueValidator`), `author` (`models.ForeignKey(Author, on_delete=models.CASCADE, null=True)`), `is_bestselling` (boolean flag with `@property best_selling` alias), and `slug` (`models.SlugField(blank=True, null=False)`).
  - **One-to-One Relationship**: Each `Author` can be linked to an `Address` (`author.address`), and each `Address` references its author (`address.author`).
  - **One-to-Many Relationship**: Books reference authors via ForeignKey. Access books through reverse relation (`author.book_set.all()`).
  - **Cascade Deletion**: When an author is deleted, all their associated books are automatically removed via `on_delete=models.CASCADE`.
- **Automatic Slug Generation**: Automatically slugifies book titles with unique ID suffixes (e.g. `harry-potter-1`) for clean and unique URLs.
- **Django Admin Integration**: `BookAdmin`, `AuthorAdmin`, and `AddressAdmin` registered with custom `list_display` and `list_filter`.
- **Automated Tests**: Unit tests covering address strings, one-to-one uniqueness and relations, author string methods, book foreign key links, cascade deletion, and `null=True` support.
- **Template Namespacing**: Clean templates stored under `book_outlet/templates/book_outlet/`:
  - `base.html`: Common layout with modern responsive CSS, header navigation, and footer.
  - `index.html`: Catalog overview listing all books with star ratings, author info, and bestseller badges.
  - `book_detail.html`: Detailed view of an individual book showing title, slug, rating, author, and bestseller status.
- **Clean URL Routing**:
  - Root path (`''`): Book list catalog.
  - Slug path (`/<slug:slug>/`): Book detail view (e.g. `/harry-potter-1/`).

---

## Project Structure

```text
book_store_using_django/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── book_store/                  # Main project configuration package
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Settings with book_outlet registered
│   ├── urls.py                  # Root URLconf mapping to book_outlet.urls
│   └── wsgi.py
└── book_outlet/                 # Book Outlet application
    ├── __init__.py
    ├── admin.py                 # Admin registration with BookAdmin, AuthorAdmin & AddressAdmin
    ├── apps.py                  # BookOutletConfig
    ├── migrations/              # Database migration files
    │   ├── 0001_initial.py
    │   ├── 0002_book_slug.py    # Slug field migration
    │   ├── 0003_author_alter_book_author.py # Author model & ForeignKey migration
    │   └── 0004_address_author_address.py   # Address model & OneToOne migration
    ├── models.py                # Address, Author & Book models (Relationships & slug logic)
    ├── templates/               # Namespaced templates
    │   └── book_outlet/
    │       ├── base.html        # Base layout & styling
    │       ├── index.html       # Book catalog list
    │       └── book_detail.html # Book details view with slug
    ├── tests.py                 # Unit tests for models & relationships
    ├── urls.py                  # App routes ('', '<slug:slug>/')
    └── views.py                 # index & book_detail views
```

---

## Setup & Local Development

### 1. Activate Environment & Install Dependencies
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Apply Database Migrations
```bash
python manage.py migrate
```

### 3. (Optional) Create Admin Superuser
```bash
python manage.py createsuperuser
```

### 4. Run Automated Tests
```bash
python manage.py test
```

### 5. Verify System
```bash
python manage.py check
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

Navigate to:
- **Books Catalog (`/`)**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Book Details (`/<slug>/`)**: [http://127.0.0.1:8000/harry-potter-1/](http://127.0.0.1:8000/harry-potter-1/)
- **Django Admin (`/admin/`)**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Interacting via Django Shell

```bash
python manage.py shell
```

```python
from book_outlet.models import Book, Author, Address

# Query all records
books = Book.objects.all()
authors = Author.objects.all()
addresses = Address.objects.all()

# Create an address
address = Address.objects.create(city="London", postal_code="SW1A 1AA", country="United Kingdom")

# Create an author linked to the address (One-to-One)
author = Author.objects.create(first_name="J.K.", last_name="Rowling", address=address)

# Create a new book linked via ForeignKey (Many-to-One)
b = Book(title="Harry Potter and the Goblet of Fire", rating=5, author=author, is_bestselling=True)
b.save()

# One-to-One: access address from author, and author from address
print(author.address)       # London, SW1A 1AA, United Kingdom
print(address.author)       # J.K. Rowling

# Many-to-One: access author from book, and all books from author
print(b.author)             # J.K. Rowling
print(author.book_set.all()) # [<Book: Harry Potter and the Goblet of Fire (5)>]
```
