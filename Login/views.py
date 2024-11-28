from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import logout

def Login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/Terry/')  # Redirige a la página principal
    else:
        form = LoginForm()
    return render(request, 'db/login.html', {'form': form})


def Logout_view(request):
    logout(request)
    return redirect('/Login/')  # Redirige al login después de cerrar sesión
