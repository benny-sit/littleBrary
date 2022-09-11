from typing_extensions import Required
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    born = models.DateField()
    about = models.TextField(max_length=2000, blank=True)
    portrait_url = models.URLField(blank=True)
    

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateField()
    book_name = models.CharField(max_length=200)
    num_pages = models.IntegerField(default=0)
    cover_url = models.URLField(blank=True)
    pdf_url = models.URLField(blank=True)
    summary = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return f'Written By: {self.author}, {self.pub_date} {self.book_name} {self.num_pages}'


class UserList(models.Model):
    list_name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_lists', null=True)
    books_list = models.ManyToManyField(Book, blank=True, related_name="books_set")
    
    
class Reviews(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='my_reviews', null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews", null=True)
    rating = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    title = models.CharField(max_length=100, default='')
    content = models.TextField(max_length=2000, blank=True)
    