from django.shortcuts import render

# Create your views here.
def Consejos(request):
    return render(request, 'db/consejos.html')
