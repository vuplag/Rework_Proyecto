from django.shortcuts import render
from django.http      import HttpResponse
# Create your views here.

def MainPG(request):
    return render(request, 'Home/home.html')