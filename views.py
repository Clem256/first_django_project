# views.py
from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def edit_book(request, val):
    book = Book.objects.get(pk=val)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})


def delete_book(request, val):
    book = Book.objects.get(pk=val)
    book.delete()
    return redirect('book_list')
