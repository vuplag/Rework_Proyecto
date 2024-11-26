from django.shortcuts import render
from django.http      import HttpResponse
# Create your views here.


def Trivia(request):
    return render(request, 'db/trivia.html')


