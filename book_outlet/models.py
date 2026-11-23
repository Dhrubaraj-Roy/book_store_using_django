from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, blank=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    @property
    def best_selling(self):
        return self.is_bestselling

    @best_selling.setter
    def best_selling(self, value):
        self.is_bestselling = value

    def get_absolute_url(self):
        return reverse("book_outlet:book-detail", args=[self.id])

    def __str__(self):
        return f"{self.title} ({self.rating})"
