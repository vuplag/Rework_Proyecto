from django.shortcuts import render

# Create your views here.

def Skins(request):
    return render(request, 'db/skins.html')