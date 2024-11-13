from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    contex ={
        'book': Book.objects.all(),

    }
    return render(request,'pages/index.html', context)

def books(request): 
    return render(request,'pages/books.html')
