from django.shortcuts import render
from books.models import Publisher, Author, Book
import datetime

def publisher(request):
    publisher_list = Publisher.objects.all()
    return render(request, 'books.html', {'publisher': publisher_list})
