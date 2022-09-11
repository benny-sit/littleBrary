from django.contrib import admin
from .models import Author, Book, UserList, Reviews
# Register your models here.


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(UserList)
admin.site.register(Reviews)