"""
URL configuration for book_store_project project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_outlet.urls')),
    path('store/', include('book_store.urls')),
]
