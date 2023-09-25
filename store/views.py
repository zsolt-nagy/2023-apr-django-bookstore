from django.shortcuts import render, redirect
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
    try:
        book = Book.objects.get(id=book_id)
        title = book.title
    except:
        book = None
        title = 'Book was not found'
    context = {
        'page': title, 
        'menu_item': 'store',
        'book': book,
        'book_id': book_id,
    }
    return render(request, 'store/book.html', context) 


def delete_book(request, book_id):  
    context = {
        'menu_item': 'store',
    }    
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        context['page'] = 'Welcome to Mystery Books'
        context['delete_successful'] = True
    except:
        context['page'] = 'Error deleting book.',
        context['delete_error'] = True
    books = Book.objects.all()       
    context['books'] = books
    context['count'] = books.count()

    return render(request, "store/store.html", context)        


def edit_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        title = book.title
    except:
        book = None
        title = 'Book was not found'
    context = {
        'page': title,
        'menu_item': 'store',
        'book': book,
        'book_id': book_id,
        'action': 'edit_book',
        'submit_button_text': 'Update Book',
        'post_error': False
    }
    if request.method == 'POST':
        try:
            book.title = request.POST.get('title')
            book.author = request.POST.get('author')
            book.description = request.POST.get('description')
            book.publish_date = request.POST.get('date_of_pub')
            book.price = request.POST.get('price')
            book.stock = request.POST.get('stock')
            book.save()
            context['update_successful'] = True
            return render(request, 'store/book.html', context) 
        except:
            context['post_error'] = True
            return render(request, 'store/book_form.html', context)
    else:
        return render(request, 'store/book_form.html', context)


def new_book(request):
    context = {
        'page': 'New Book',
        'menu_item': 'store',
        'create_successful': False,
        'post_error': False,
        'action': 'new_book',
        'submit_button_text': 'Add Book',
    }
    if request.method == 'POST':
        try:
            new_book = Book(
                title = request.POST.get('title'),
                author = request.POST.get('author'),
                description = request.POST.get('description'),
                publish_date = request.POST.get('date_of_pub'),
                price = request.POST.get('price'),
                stock = request.POST.get('stock')
            )
            new_book.save()
            context['create_successful'] = True
        except:
            context['post_error'] = True
        return render(request, 'store/book_form.html', context)
    else:
        return render(request, 'store/book_form.html', context)