from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    
    path('authors/', views.author, name='authors'),
    path('create_author', views.create_author, name='create_author'),
    path('author/<int:id>', views.author_id, name='author_id'),
    path('update_author/<int:id>', views.update_author, name='update_author'),
    
    path('book/<int:id>', views.view_book, name='book_id'),
    path('books/', views.books, name='books'),
    path('update_book/<int:id>', views.update_book, name='update_book'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
    
    path('lists/', views.lists, name='my_lists'),
    path('create_list', views.create_list, name='create_list'),
    path('delete_list/<int:id>', views.delete_list, name='delete_list'),
    path('open_list/<int:id>', views.open_list, name='open_list'),
    
    path('update_review/<int:book_id>', views.update_review, name='update_review'),
    path('delete_review/<int:book_id>', views.delete_review, name='delete_review'),
    path('create_review/<int:book_id>', views.create_review, name='create_review'),
]