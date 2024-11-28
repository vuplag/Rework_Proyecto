from django.shortcuts import render, redirect
from .forms import RegistroForm

def Register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Login/')  # Redirige al login después del registro
    else:
        form = RegistroForm()
    return render(request, 'db/register.html', {'form': form})
