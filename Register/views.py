from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Vista para el registro
def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')  # Redirigir al login después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'db/index.html', {'form': form})