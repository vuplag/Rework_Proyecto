from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile



@login_required
def Terry(request):

    profile = UserProfile.objects.get(user=request.user)
    context = {
        'active_skin': profile.active_skin
    }
    return render(request, 'db/mainterry.html', context)







@login_required
def Consejos(request):

    profile = UserProfile.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'db/consejos.html', context)






@login_required
def Trivia(request):

    profile = UserProfile.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'db/trivia.html', context)






@login_required
def Skins(request):
    
    profile = UserProfile.objects.get(user=request.user)
    context = {
        'trivias_completed': profile.trivias_completed,  
        'active_skin': profile.active_skin,              
    }
    return render(request, 'db/skins.html', context)






@login_required
def SeleccionarSkin(request, skin_name):

    profile = UserProfile.objects.get(user=request.user)
    
    if skin_name == "Pinguino.gif" and profile.trivias_completed < 5:
        return HttpResponse("No tienes suficientes trivias completadas para esta skin.", status=403)
    

    if skin_name == "Deathstarskin.gif" and profile.trivias_completed < 10:
        return HttpResponse("No tienes suficientes trivias completadas para esta skin.", status=403)
    
    
    profile.active_skin = skin_name
    profile.save()

    return render(request, 'db/skins.html', {'profile': profile, 'trivias_completed': profile.trivias_completed})