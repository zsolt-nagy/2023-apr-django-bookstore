from django.shortcuts import render
from .models import Book


# Create your views here.
def index(request):
    return render(request, 'store/template.html')


def store(request):
   count = Book.objects.all().count()
   context = {
       'count': count,
       'count2': count - 2,
   }
   return render(request, "store/store.html", context)


