from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    @property
    def best_selling(self):
        return self.is_bestselling

    @best_selling.setter
    def best_selling(self, value):
        self.is_bestselling = value

    def get_absolute_url(self):
        return reverse("book_outlet:book-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            if not self.id:
                super().save(*args, **kwargs)
            self.slug = f"{slugify(self.title)}-{self.id}"
            super().save(update_fields=["slug"])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
