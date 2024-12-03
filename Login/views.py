from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import logout
from Terry.models        import UserProfile

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

def reset(request):
    profile = UserProfile.objects.get(user = request.user)

    profile.trivias_completed         = 0
    profile. lives                    = 3
    profile.active_skin               = "TerryNice"
    profile.consecutive_trivias       = 0
    profile.last_trivia_date          = None
    profile.consecutive_failedtrivias = 0

    profile.save()

    logout(request)

    return redirect('/Login/')