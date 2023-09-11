from django.shortcuts import render
from .models import Book


# Create your views here.
def index(request):
    context = {
        'page': 'Mystery Books',
        'menu_item': 'index'
    }
    return render(request, 'store/template.html', context)


def store(request):
   books = Book.objects.all()
   count = books.count()
   context = {
       'count': count,
       'books': books,
       'page': 'Welcome to Mystery Books',
       'menu_item': 'store'
   }
   return render(request, "store/store.html", context)

def display_book(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'page': book.title, 
        'menu_item': book.title,
        'book': book
    }
    return render(request, 'store/template.html', context) # TODO: write new template