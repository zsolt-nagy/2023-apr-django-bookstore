from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('store/<int:book_id>', views.display_book, name='display_book'),
    path('store/new', views.new_book, name='new_book'),
]