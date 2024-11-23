from django.shortcuts            import render, redirect
from django.contrib.auth         import authenticate, login, logout
from django.contrib.auth.forms   import UserCreationForm, AuthenticationForm
from django.http                 import HttpResponse


def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirigir al home después de hacer login
    else:
        form = AuthenticationForm()
    return render(request, 'db/login.html', {'form': form})

