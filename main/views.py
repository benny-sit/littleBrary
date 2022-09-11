from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Author, Book, UserList
from .forms import CreateNewAuthor, CreateNewBook, CreateUserList, CreateReview
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(req):
    return render(req, 'main/home.html', {})


def author(req):
    if req.method == "POST":
        for k, v in req.POST.items():
            if 'c' == k[0] and v == 'clicked':
                Author.objects.filter(id=k[1:]).delete()

    f = CreateNewAuthor()
    authors = Author.objects
    return render(req, 'main/authors.html', {"authors": authors, "form": f})

@login_required(login_url="/login")
def update_author(req, id):
    if Author.objects.filter(id=id).exists():
        print("author already exists")
        if req.method == 'POST':
            print("POST REq")
            f = CreateNewAuthor(req.POST, instance=Author.objects.get(id=id))
            if f.is_valid():
                f.save()
        else:
            f = CreateNewAuthor(instance=Author.objects.get(id=id))
            return render(req, 'main/updateAuthors.html', {'form': f, 'id': id})
    
    return redirect('authors')

@login_required(login_url="/login")
def create_author(req):
    if req.method == "POST" and req.user.is_authenticated:
        f = CreateNewAuthor(req.POST)
        if f.is_valid():
            f.save()
            
    return redirect('/authors')

def author_id(req, id):
    if Author.objects.filter(id=id).exists():
        return render(req, 'main/authorCard.html', {"author": Author.objects.get(id=id)})
    
    return redirect('authors')


def books(req):
    if req.method == "POST" and req.user.is_authenticated:
        f_data = req.POST.copy()
        f_data["author"] = Author.objects.get(id=f_data["author"])
        f = CreateNewBook(f_data)
        if f.is_valid():
            print("Author created")
            f.save()
        return redirect('books')
            
    return render(req, 'main/books.html', {"books": Book.objects, "form": CreateNewBook})


def view_book(req, id):
    if Book.objects.filter(id=id).exists():
        b = Book.objects.get(id=id)
        
        edit = b.reviews.filter(owner=req.user).exists()
        if edit:
            f = CreateReview(instance=b.reviews.get(owner=req.user))
        else:
            f = CreateReview()
        return render(req, 'main/bookCard.html', {"book": Book.objects.get(id=id), "form": f, "edit": edit})
    
    return redirect('books')


@login_required(login_url='/login')
def delete_book(req, id):
    b = Book.objects.get(id=id)
    b.delete()
    return redirect('books')


@login_required(login_url='/login')
def update_book(req, id):
    if Book.objects.filter(id=id).exists():
        if req.method == 'POST':
            f = CreateNewBook(req.POST, instance=Book.objects.get(id=id))
            if f.is_valid():
                f.save()
            return redirect('/books')
            
        f = CreateNewBook(instance=Book.objects.get(id=id))
        
        return render(req, 'main/updateBooks.html', {"form": f , 'id': id})
    
    return redirect('/books')


@login_required(login_url='/login')
def lists(req):
    print(req.user.my_lists.all())
    return render(req, 'main/lists.html', {"lists": req.user.my_lists})


@login_required(login_url='/login')
def create_list(req):
    if req.method == 'POST':
        f = CreateUserList(req.POST)
        if f.is_valid():
            event = f.save(commit=False)
            event.owner = req.user
            event.save()
            return redirect('my_lists')
    
    f = CreateUserList()
    return redirect('my_lists')


@login_required(login_url='/login')
def delete_list(req, id):
    if req.user.my_lists.filter(id=id).exists:
        req.user.my_lists.filter(id=id).delete()
        
    return redirect('my_lists')


@login_required(login_url='/login')
def open_list(req, id):
    l = req.user.my_lists.filter(id=id)
    if l.exists and l[0]:
        if req.method == 'POST':
            for k, v in req.POST.items():
                if k[0] == 'a' and v == 'add':
                    l[0].books_list.add(Book.objects.get(id=k[1:]))
                    l[0].save()
                if k[0] == 'r' and v == 'remove':
                    l[0].books_list.remove(Book.objects.get(id=k[1:]))
                    l[0].save()
        return render(req, 'main/myList.html', { 'my_list': l[0], 'books': Book.objects})
    
    return redirect('my_lists')


@login_required(login_url='/login')
def create_review(req, book_id):
    if req.method == 'POST' and Book.objects.filter(id=book_id).exists():
        b = Book.objects.get(id=book_id)
        if not b.reviews.filter(owner=req.user).exists():
            f = CreateReview(req.POST)
            if f.is_valid():
                event = f.save(commit=False)
                event.owner = req.user
                event.book = Book.objects.get(id=book_id)
                event.save()
        return redirect('book_id', id=book_id)
    return redirect('books')


@login_required(login_url='/login')
def update_review(req, book_id):
    if Book.objects.filter(id=book_id).exists():
        if req.method == 'POST':
            b = Book.objects.get(id=book_id)
            f = CreateReview(req.POST, instance=b.reviews.get(owner=req.user))
            if f.is_valid():
                event = f.save(commit=False)
                event.owner = req.user
                event.book = Book.objects.get(id=book_id)
                event.save()
            
        return redirect('book_id', id=book_id)
            
    return redirect('books')
        


@login_required(login_url='/login')
def delete_review(req, book_id):
    if Book.objects.filter(id=book_id).exists():
        b = Book.objects.get(id=book_id)
        if b.reviews.filter(owner=req.user).exists():
            r = b.reviews.get(owner=req.user)
            r.delete()
    return redirect('book_id', id=book_id)