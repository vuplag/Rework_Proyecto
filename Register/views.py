from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistroForm

# Vista para el registro
def Register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Login')  # Redirigir al login después de registrarse
    else:
        form = RegistroForm()
    return render(request, 'db/index.html', {'form': form})