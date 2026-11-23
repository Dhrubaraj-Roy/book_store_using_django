# Book Store Using Django

A full-featured Django project containing two dedicated applications:
- **`book_outlet`**: Outlets catalog management, `Book` model with rating validators, Django Admin integration, and responsive HTML templates.
- **`book_store`**: Primary store services, catalog routing, and modular expansion.

---

## Features

- **Modular Architecture**: Separate apps for `book_outlet` and `book_store` registered in `INSTALLED_APPS`.
- **Database Model**: `Book` model with `title`, `rating` (1–5 scale with `MinValueValidator` and `MaxValueValidator`), `author`, and `is_bestselling` (boolean flag with `@property best_selling` alias).
- **Django Admin Integration**: `BookAdmin` with custom `list_display` (`title`, `author`, `rating`, `is_bestselling`).
- **Template Namespacing**: Clean templates stored under `book_outlet/templates/book_outlet/`:
  - `base.html`: Common layout with modern responsive CSS, header navigation, and footer.
  - `index.html`: Catalog overview listing all books with star ratings, author info, and bestseller badges.
  - `book_detail.html`: Detailed view of an individual book showing all fields with navigation controls.
- **Clean URL Routing**: Root path (`''`) serves the book list view directly.

---

## Project Structure

```text
book_store_using_django/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── book_store_project/          # Main project configuration package
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # INSTALLED_APPS, TEMPLATES, database settings
│   ├── urls.py                  # Root URLconf mapping to book_outlet.urls
│   └── wsgi.py
├── book_outlet/                 # Book Outlet application
│   ├── __init__.py
│   ├── admin.py                 # Admin registration with BookAdmin
│   ├── apps.py                  # BookOutletConfig
│   ├── migrations/              # Database migration files
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py                # Book model
│   ├── templates/               # Namespaced templates
│   │   └── book_outlet/
│   │       ├── base.html        # Base skeleton & styles
│   │       ├── index.html       # Book catalog list
│   │       └── book_detail.html # Book details view
│   ├── tests.py
│   ├── urls.py                  # App routes ('', '<int:id>/')
│   └── views.py                 # index & book_detail views
└── book_store/                  # Book Store application
    ├── __init__.py
    ├── admin.py
    ├── apps.py                  # BookStoreConfig
    ├── migrations/
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

---

## Setup & Local Development

### 1. Clone & Set Up the Environment
```bash
git clone https://github.com/Dhrubarajroy/book_store_using_django.git
cd book_store_using_django

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
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

### 4. Verify System
```bash
python manage.py check
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

Navigate to:
- **Books Catalog (`/`)**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Book Details (`/<id>/`)**: [http://127.0.0.1:8000/1/](http://127.0.0.1:8000/1/)
- **Django Admin (`/admin/`)**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Interacting via Django Shell

You can query, create, and inspect records interactively in the Django shell:

```bash
python manage.py shell
```

```python
from book_outlet.models import Book

# 1. Query all records (table access)
books = Book.objects.all()
print(books)

# 2. Create new book records
b = Book(title="Harry Potter", rating=5, author="J.K. Rowling", is_bestselling=True)
b.save()

Book.objects.create(title="The Hobbit", rating=4, author="J.R.R. Tolkien", is_bestselling=True)

# 3. Access specific record attributes
book = Book.objects.first()
print(book.title)           # Title
print(book.rating)          # Rating (1-5)
print(book.author)          # Author
print(book.is_bestselling)   # Best-selling boolean
print(book.best_selling)    # Property alias

# 4. Filter records
bestsellers = Book.objects.filter(is_bestselling=True)
top_rated = Book.objects.filter(rating__gte=4)
```
