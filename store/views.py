from django.shortcuts import render
from .models import Book


# Create your views here.
def index(request):
    context = {
        'page': 'Mystery Books'
    }
    return render(request, 'store/template.html', context)


def store(request):
   count = Book.objects.all().count()
   context = {
       'count': count,
       'page': 'Welcome to Mystery Books'
   }
   return render(request, "store/store.html", context)


