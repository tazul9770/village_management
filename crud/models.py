from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='authors')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name='categories')

    def __str__(self):
        return self.name

class BookDetail(models.Model):
    summary = models.TextField()
    isbn = models.CharField(max_length=20, unique=True)
    pages = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='detail')

    def __str__(self):
        return f"Details for ISBN {self.isbn}"
