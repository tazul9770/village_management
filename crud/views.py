from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from crud.models import Book, Author, BookDetail, Category

def show_data(request):
    # all books retrive
    # books = Book.objects.all()

    # nirdishto writer kono book likhce kina 
    #authors = Author.objects.filter(name='Frank Herbert').first().book

    # page 300 er beshi or kom oi sob book
    # books = BookDetail.objects.filter(pages__lt = 300) 
    # books = BookDetail.objects.filter(pages__gt = 300) 

    # j sob book er namer modde war likha ache
    #books  = Book.objects.filter(title__icontains='war')

    #order by title
    #books = Book.objects.order_by("title")
    #books = Book.objects.order_by("-title")

    # all bokks use select related
    #books  = Book.objects.select_related('authors').all()
    #books = Author.objects.select_related('book').all()

    # books details see use prefatch related, 
    #books = BookDetail.objects.prefetch_related('book').all()

    # many to many prefetch related use
    #books = Book.objects.prefetch_related('categories').all()

    # category onojayi koto book ache 
    #books = Category.objects.annotate(total_books=Count('books'))

    # j sob book er category akadhik
    #books = Book.objects.annotate(category_count=Count('categories')).filter(category_count__gt=1)

    return render(request, 'show_data.html', {'books':books})
