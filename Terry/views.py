from django.shortcuts import render
from django.http      import HttpResponse
# Create your views here.

def Terry(request):
    return render(request, 'db\mainterry.html')